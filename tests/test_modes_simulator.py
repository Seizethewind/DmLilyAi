"""Request modes (Chat / Manage / Analyst / Simulator) and the veteran simulator, through the real router.

No network and no API keys: a scripted provider stands in for the model and for the vision model.
The simulator tests use the real data in tools/sim_data and skip themselves if it is missing.

Run:  python -m unittest tests.test_modes_simulator -v     (or the whole suite: python -m unittest discover -s tests -v)
"""
import asyncio
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse, ToolCallRequest  # noqa: E402
from LilyAiMain.MainService.bootstrap import App, build_app  # noqa: E402
from LilyAiMain.MainService.Interaction.messages import ImageAttachment, IncomingMessage  # noqa: E402
from LilyAiMain.MainService.Interaction.Modes import MODES, match_switch, mode_menu  # noqa: E402
from LilyAiMain.MainService.Interaction.Modes.modes import CURRENT_RE, MENU_RE  # noqa: E402
from LilyAiMain.MainService.Interaction.Workflows.chat_workflow import ChatRequest  # noqa: E402
from LilyAiMemory.Veteran.veteran_store import MAX_RESULTS_PER_VETERAN, MAX_VETERANS, VeteranLimitError  # noqa: E402
from LilyAiTool.Models.tool_models import ToolContextData  # noqa: E402

_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


VET_FILE = ROOT / "LilyAiGameSpace" / "Umamusume" / "Simulation" / "Veteran" / "veteran_oguri_cap.json"
COURSE = "10606"   # the course the Simulator's own demo uses


def oguri() -> dict:
    return json.loads(VET_FILE.read_text(encoding="utf-8"))


class ModeProvider(LLMProvider):
    """Records every chat call. Can be told to request one tool; answers vision (image) calls with a veteran."""

    def __init__(self):
        self.calls = []
        self.tool_to_call: str | None = None
        self.vet_json = {"is_veteran": True, **oguri()}

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        last = messages[-1]
        if isinstance(last["content"], list):   # a screenshot
            self.calls.append({"vision": True})
            return LLMResponse(json.dumps(self.vet_json), model=model or "")
        if json_mode:                            # background fact extraction
            return LLMResponse('{"facts": []}')
        self.calls.append({
            "vision": False, "tools": [t["function"]["name"] for t in (tools or [])],
            "prompt": "\n".join(str(m.get("content", "")) for m in messages),
        })
        if last["role"] == "tool":
            return LLMResponse(f"TOOL SAID: {last['content']}", model=model or "")
        if self.tool_to_call and tools:
            name, self.tool_to_call = self.tool_to_call, None
            raw = {"role": "assistant", "content": "", "tool_calls": [
                {"id": "c1", "type": "function", "function": {"name": name, "arguments": "{}"}}]}
            return LLMResponse("", [ToolCallRequest("c1", name, {})], model or "", raw_message=raw)
        return LLMResponse("A plain reply from Lily that is long enough to look like a real answer.", model=model or "")

    async def list_models(self):
        return []

    def chat_calls(self):
        return [c for c in self.calls if not c["vision"]]


class AppCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.environ["LILYAI_DATA_DIR"] = self.tmp
        os.environ["GROQ_API_KEY"] = ""
        self.provider = ModeProvider()
        self.app: App = build_app(load_settings(), provider=self.provider, search_provider=object())

    def user(self, uid):
        self.app.memory.user.add(uid, "Test user")   # skips onboarding
        return uid

    def say(self, uid, text):
        return run(self.app.router.route(IncomingMessage(uid, text, "Tester", "simulator")))

    def send_images(self, uid, n=1):
        images = [ImageAttachment(b"\x89PNG fake", "image/png", f"shot{i}.png") for i in range(n)]
        return run(self.app.router.route(IncomingMessage(uid, "", "Tester", "simulator", images=images)))


# ---------------------------------------------------------------------------------------------- pure patterns
class ModePatternTests(unittest.TestCase):
    def test_switch_phrases(self):
        for text, key in [
            ("simulator mode", "simulator"), ("Simulator Mode", "simulator"), ("sim mode", "simulator"),
            ("switch to manage mode", "manage"), ("Switch to Analyst Mode.", "analyst"),
            ("please go to the analyst mode", "analyst"), ("chat mode", "chat"), ("use simulator mode!", "simulator"),
        ]:
            self.assertEqual(match_switch(text), key, text)

    def test_switch_is_not_triggered_by_ordinary_sentences(self):
        for text in [
            "what is simulator mode", "tell me about analyst mode please", "analyst", "I like chat mode a lot",
            "how do I switch to manage mode", "simulate Oguri Cap",
        ]:
            self.assertIsNone(match_switch(text), text)

    def test_menu_and_current(self):
        for text in ["mode", "Modes", "show modes", "switch mode", "which mode?", "what modes do you have"]:
            self.assertTrue(MENU_RE.match(text), text)
        self.assertTrue(CURRENT_RE.match("what mode am I in?"))
        for text in ["mode of transport", "modern art", "simulator mode"]:
            self.assertFalse(MENU_RE.match(text), text)

    def test_menu_buttons_round_trip(self):
        items = mode_menu()
        self.assertEqual([i.label for i in items], [m.label for m in MODES.values()])
        for item, mode in zip(items, MODES.values()):
            self.assertEqual(match_switch(item.text), mode.key)


# ---------------------------------------------------------------------------------------------- the router
class ModeRouterTests(AppCase):
    def test_mode_shows_four_buttons(self):
        uid = self.user("m1")
        out = self.say(uid, "mode")
        self.assertEqual(out[0].kind, "system")
        self.assertIn("Chat Mode", out[0].text)
        self.assertEqual(len(out[0].menu), 4)
        self.assertEqual(self.provider.chat_calls(), [], "the mode menu must not reach the model")

    def test_switching_persists_and_is_answered_by_code(self):
        uid = self.user("m2")
        out = self.say(uid, "simulator mode")
        self.assertIn("Switched to **Simulator Mode**", out[0].text)
        self.assertEqual(self.provider.chat_calls(), [])
        self.assertIn("Simulator Mode", self.say(uid, "what mode am I in?")[0].text)
        self.say(uid, "manage mode")
        self.assertEqual(self.app.memory.session.get(uid).data["mode"], "manage")

    def _doc_snippet(self):
        """The passage the game docs inject for 'Special Week' (what Lily used to answer from on every turn)."""
        from LilyAiGameSpace.UmamusumeGameSpaceEngine import get_engine
        snippets = get_engine().context_for("Special Week")
        if not snippets:
            self.skipTest("game docs not indexed here")
        return snippets[0][:80]

    def test_default_is_chat_with_web_and_without_game_docs(self):
        snippet = self._doc_snippet()
        uid = self.user("m3")
        self.say(uid, "tell me about Special Week")
        call = self.provider.chat_calls()[-1]
        self.assertIn("web_search", call["tools"])
        self.assertFalse([t for t in call["tools"] if t.startswith(("game_docs", "sim_", "my_"))], call["tools"])
        self.assertIn("game docs are not loaded", call["prompt"])
        self.assertNotIn(snippet, call["prompt"], "Chat Mode must not inject the game docs")

    def test_each_mode_offers_only_its_tools(self):
        expect = {
            "chat": ({"web_search", "calculate"}, {"game_docs_search", "sim_run", "get_linked_trainer"}),
            "manage": ({"get_linked_trainer", "remind_me"}, {"web_search", "game_docs_search", "sim_run"}),
            "analyst": ({"game_docs_search", "game_docs_read", "my_cards"}, {"web_search", "sim_run", "get_linked_trainer"}),
            "simulator": ({"sim_run", "sim_list_veterans"}, {"web_search", "game_docs_search", "get_linked_trainer"}),
        }
        uid = self.user("m4")
        for key, (present, absent) in expect.items():
            self.say(uid, f"{key} mode")
            self.say(uid, "hello there, how are you doing today")
            tools = set(self.provider.chat_calls()[-1]["tools"])
            self.assertTrue(present <= tools, f"{key}: missing {present - tools}")
            self.assertFalse(absent & tools, f"{key}: should not have {absent & tools}")

    def test_analyst_mode_loads_the_game_docs(self):
        snippet = self._doc_snippet()
        uid = self.user("m5")
        self.say(uid, "analyst mode")
        self.say(uid, "tell me about Special Week")
        call = self.provider.chat_calls()[-1]
        self.assertIn("game_docs_search", call["tools"])
        self.assertIn(snippet, call["prompt"])

    def test_a_tool_from_another_mode_is_refused_not_run(self):
        uid = self.user("m6")
        # In Chat Mode game_docs_search is not offered, but a model could still ask for it by name.
        self.provider.tool_to_call = "game_docs_search"
        out = run(self.app.chat.handle(ChatRequest(uid, "hi", "T", "chat")))
        self.assertIn("isn't available in Chat Mode", out.text)
        self.assertEqual(out.tools_used, [], "a refused call must not be reported as used")

    def test_tip_offers_another_mode_once(self):
        uid = self.user("m7")
        out = self.say(uid, "can you simulate my veteran on a course?")
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].kind, "chat")
        self.assertIn("Simulator Mode", out[1].text)
        self.assertEqual(out[1].menu[0].text, "switch to simulator mode")
        self.assertEqual(len(self.say(uid, "simulate it again please")), 1, "the tip is shown once per mode per session")
        # the button text really switches
        self.assertIn("Switched to **Simulator Mode**", self.say(uid, out[1].menu[0].text)[0].text)

    def test_no_tip_when_already_in_that_mode(self):
        uid = self.user("m8")
        self.say(uid, "simulator mode")
        self.assertEqual(len(self.say(uid, "simulate a veteran for me")), 1)

    def test_naming_a_character_in_simulator_mode_does_not_suggest_analyst(self):
        # "Oguri Cap" is a game-doc name, but in Simulator Mode it is just the veteran being simulated.
        uid = self.user("m10")
        self.say(uid, "simulator mode")
        self.assertEqual(len(self.say(uid, "simulate Oguri Cap on Tokyo 2400 turf")), 1)

    def test_chat_mode_suggests_analyst_for_a_doc_question_once(self):
        self._doc_snippet()
        uid = self.user("m11")
        out = self.say(uid, "tell me about Special Week")
        self.assertEqual(len(out), 2)
        self.assertEqual(out[1].menu[0].text, "switch to analyst mode")
        self.assertEqual(len(self.say(uid, "and what about Special Week's skills?")), 1)

    def test_forget_me_wipes_veterans(self):
        uid = self.user("m9")
        self.app.memory.veterans.save(uid, oguri())
        self.say(uid, "forget everything about me")
        self.say(uid, "yes")
        self.assertEqual(self.app.memory.veterans.list(uid), [])


# ---------------------------------------------------------------------------------------------- the store
class VeteranStoreTests(AppCase):
    def setUp(self):
        super().setUp()
        self.store = self.app.memory.veterans

    def test_create_then_unchanged_then_merge_skills(self):
        vet = oguri()
        self.assertEqual(self.store.save("u", vet), (1, "created"))
        self.assertEqual(self.store.save("u", vet), (1, "unchanged"))
        more = oguri()
        more["skills"] = [*more["skills"], "Corner Recovery ○"]
        self.assertEqual(self.store.save("u", more), (1, "updated"))
        saved = self.store.get("u", 1)["vet"]
        self.assertEqual(len(saved["skills"]), len(vet["skills"]) + 1)

    def test_same_name_different_stats_is_a_new_veteran(self):
        self.store.save("u", oguri())
        other = oguri()
        other["stats"]["speed"] += 10
        self.assertEqual(self.store.save("u", other), (2, "created"))
        self.assertEqual([r["vet_id"] for r in self.store.find("u", "Oguri Cap")], [1, 2])
        self.assertEqual([r["vet_id"] for r in self.store.find("u", "#2")], [2])
        self.assertEqual([r["vet_id"] for r in self.store.find("u", "oguri")], [1, 2])

    def test_users_are_isolated(self):
        self.store.save("a", oguri())
        self.assertEqual(self.store.list("b"), [])
        self.assertEqual(self.store.find("b", "Oguri Cap"), [])
        self.assertIsNone(self.store.get("b", 1))
        self.assertEqual(self.store.save("b", oguri()), (1, "created"), "ids are per user")

    def test_limit(self):
        for i in range(MAX_VETERANS):
            v = oguri()
            v["stats"]["speed"] = 500 + i
            self.store.save("u", v)
        extra = oguri()
        extra["stats"]["speed"] = 5
        with self.assertRaises(VeteranLimitError):
            self.store.save("u", extra)
        self.assertEqual(len(self.store.list("u")), MAX_VETERANS)

    def test_results_are_capped_and_deleted_with_the_veteran(self):
        self.store.save("u", oguri())
        for i in range(MAX_RESULTS_PER_VETERAN + 5):
            self.store.add_result("u", 1, COURSE, f"run {i}")
        self.assertEqual(self.store.result_count("u", 1), MAX_RESULTS_PER_VETERAN)
        self.assertEqual(self.store.results("u", 1, 1)[0]["summary"], f"run {MAX_RESULTS_PER_VETERAN + 4}")
        self.assertTrue(self.store.delete("u", 1))
        self.assertEqual(self.store.result_count("u", 1), 0)
        self.assertFalse(self.store.delete("u", 1))

    def test_clear_only_touches_one_user(self):
        self.store.save("a", oguri())
        self.store.save("b", oguri())
        self.assertEqual(self.store.clear("a"), 1)
        self.assertEqual(len(self.store.list("b")), 1)


# ---------------------------------------------------------------------------------------------- simulator tools
def _sim_ready() -> bool:
    try:
        from LilyAiGameSpace.Umamusume.Simulation import sim_service
        return sim_service.is_available()
    except Exception:
        return False


@unittest.skipUnless(_sim_ready(), "tools/sim_data (skills.json, courses.json) not found")
class SimulatorToolTests(AppCase):
    def tool(self, name, args, uid="u1"):
        return run(self.app.tools.run(name, args, ToolContextData(uid, "Tester")))

    def test_tools_are_registered_in_the_simulator_category_only(self):
        sims = {n for n, s in self.app.tools.registry._tools.items() if s.category == "simulator"}
        self.assertEqual(sims, {"sim_list_veterans", "sim_find_skill", "sim_list_courses", "sim_run"})

    def test_list_veterans_empty_then_filled(self):
        self.assertIn("no saved veterans", self.tool("sim_list_veterans", {}).output)
        self.app.memory.veterans.save("u1", oguri())
        out = self.tool("sim_list_veterans", {}).output
        self.assertIn("#1 Oguri Cap", out)
        self.assertIn("1608/747/1250/623/775", out)

    def test_course_and_skill_lookup(self):
        out = self.tool("sim_list_courses", {"query": "tokyo"}).output
        self.assertRegex(out, r"\d+: Tokyo \d+m (turf|dirt)")
        self.assertIn("Corner Recovery", self.tool("sim_find_skill", {"query": "corner recovery"}).output)
        self.assertIn("No skill name contains", self.tool("sim_find_skill", {"query": "zzzzqqq"}).output)
        self.assertFalse(self.tool("sim_find_skill", {}).ok, "query is required")

    def test_run_one_build(self):
        self.app.memory.veterans.save("u1", oguri())
        res = self.tool("sim_run", {"veteran": "1", "course": COURSE, "runs": 50})
        self.assertTrue(res.ok, res.output)
        self.assertIn("Oguri Cap", res.output)
        self.assertIn("A (as saved): mean", res.output)
        self.assertIn("50 runs", res.output)
        self.assertIn("Model limits", res.output, "the caveat must survive the 4000-char output cap")
        self.assertEqual(self.app.memory.veterans.result_count("u1", 1), 1)

    def test_run_is_repeatable(self):
        self.app.memory.veterans.save("u1", oguri())
        a = self.tool("sim_run", {"veteran": "Oguri Cap", "course": COURSE, "runs": 50}).output
        b = self.tool("sim_run", {"veteran": "Oguri Cap", "course": COURSE, "runs": 50}).output
        self.assertEqual(a, b, "seeded, so the same request gives the same numbers")

    def test_run_compares_added_skills_and_warns_about_unknown_ones(self):
        self.app.memory.veterans.save("u1", oguri())
        res = self.tool("sim_run", {"veteran": "1", "course": COURSE, "runs": 50,
                                    "add_skills": ["Corner Recovery ○", "Totally Made Up Skill"]})
        self.assertTrue(res.ok, res.output)
        self.assertIn("B vs A", res.output)
        self.assertIn("Warnings:", res.output)
        self.assertIn("Totally Made Up Skill", res.output)

    def test_run_clamps_tiny_run_counts(self):
        self.app.memory.veterans.save("u1", oguri())
        self.assertIn("50 runs", self.tool("sim_run", {"veteran": "1", "course": COURSE, "runs": 1}).output)

    def test_run_errors_are_plain_messages(self):
        self.assertIn("No saved veteran", self.tool("sim_run", {"veteran": "Oguri Cap", "course": COURSE}).output)
        self.app.memory.veterans.save("u1", oguri())
        self.assertFalse(self.tool("sim_run", {"veteran": "1", "course": "no-such-course", "runs": 50}).ok)
        self.assertFalse(self.tool("sim_run", {"veteran": "1"}).ok, "course is required")

    def test_ambiguous_name_asks_instead_of_guessing(self):
        self.app.memory.veterans.save("u1", oguri())
        other = oguri()
        other["stats"]["speed"] += 1
        self.app.memory.veterans.save("u1", other)
        res = self.tool("sim_run", {"veteran": "Oguri Cap", "course": COURSE, "runs": 50})
        self.assertFalse(res.ok)
        self.assertIn("#1", res.output)
        self.assertIn("#2", res.output)

    def test_a_user_cannot_simulate_someone_elses_veteran(self):
        self.app.memory.veterans.save("owner", oguri())
        self.assertIn("no saved veterans", self.tool("sim_list_veterans", {}, uid="intruder").output)
        res = self.tool("sim_run", {"veteran": "1", "course": COURSE, "runs": 50}, uid="intruder")
        self.assertFalse(res.ok)
        self.assertEqual(self.app.memory.veterans.result_count("owner", 1), 0)


# ---------------------------------------------------------------------------------------------- screenshots
@unittest.skipUnless(_sim_ready(), "tools/sim_data (skills.json, courses.json) not found")
class ImageRoutingTests(AppCase):
    def test_simulator_mode_saves_the_veteran_for_this_user(self):
        uid = self.user("i1")
        self.say(uid, "simulator mode")
        out = self.send_images(uid, n=2)   # two screenshots of the same veteran merge into one
        self.assertIn("Saved as veteran #1 (created)", out[0].text)
        self.assertEqual([r["name"] for r in self.app.memory.veterans.list(uid)], ["Oguri Cap"])
        self.assertEqual(self.app.memory.veterans.list("someone-else"), [])
        again = self.send_images(uid)
        self.assertIn("(unchanged)", again[0].text)
        self.assertEqual(len(self.app.memory.veterans.list(uid)), 1)

    def test_a_non_veteran_image_is_not_saved(self):
        uid = self.user("i2")
        self.say(uid, "simulator mode")
        self.provider.vet_json = {"is_veteran": False}
        out = self.send_images(uid)
        self.assertIn("couldn't find a veteran", out[0].text)
        self.assertEqual(self.app.memory.veterans.list(uid), [])

    def test_other_modes_keep_the_career_review(self):
        uid = self.user("i3")
        for mode in ("chat", "analyst"):
            self.say(uid, f"{mode} mode")
            out = self.send_images(uid)
            self.assertNotIn("Saved as veteran", out[0].text, mode)
            self.assertEqual(self.app.memory.veterans.list(uid), [], mode)


if __name__ == "__main__":
    unittest.main()
