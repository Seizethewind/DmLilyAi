"""Screenshots through the real router (built the same way as test_smoke.py).

NOT RUN when it was written: it needs the full app, which the sandbox it was written in did not have. Run it with
    python -m unittest discover -s tests -v
"""
import asyncio
import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, os.path.dirname(__file__))

try:  # allow running the tests without httpx installed
    import httpx  # noqa: F401
except ImportError:
    sys.modules["httpx"] = types.SimpleNamespace(AsyncClient=object, HTTPError=Exception)

from LilyAiCore.Config.settings import load_settings  # noqa: E402
from LilyAiCore.Providers.base import LLMProvider, LLMResponse  # noqa: E402
from LilyAiMain.MainService.bootstrap import App, build_app  # noqa: E402
from LilyAiMain.MainService.Interaction.messages import ImageAttachment, IncomingMessage  # noqa: E402
from test_career_evaluator import falcon_extraction  # noqa: E402


class VisionProvider(LLMProvider):
    """Answers any request that carries an image with a trainee-sheet JSON; everything else plainly."""

    def __init__(self):
        self.vision_calls = []

    async def chat(self, messages, *, model=None, tools=None, temperature=0.6, max_tokens=None, json_mode=False, fallback=True):
        if isinstance(messages[-1]["content"], list):
            self.vision_calls.append({"model": model, "fallback": fallback, "json": json_mode})
            return LLMResponse(json.dumps(falcon_extraction()), model=model or "")
        if json_mode:
            return LLMResponse('{"facts": []}')
        return LLMResponse("Hello from Lily, happy to help with whatever you need today.", model=model or "")

    async def list_models(self):
        return []


_LOOP = asyncio.new_event_loop()


def run(coro):
    return _LOOP.run_until_complete(coro)


class CareerReviewRouterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        os.environ["LILYAI_DATA_DIR"] = self.tmp
        os.environ["GROQ_API_KEY"] = ""
        self.provider = VisionProvider()
        self.app: App = build_app(load_settings(), provider=self.provider, search_provider=object())

    def shot(self, uid, text="", n=1):
        images = [ImageAttachment(b"\x89PNG fake", "image/png", f"{i}.png") for i in range(n)]
        return run(self.app.router.route(IncomingMessage(uid, text, "Tester", "simulator", images)))

    def test_screenshot_gets_a_review_without_onboarding(self):
        out = self.shot("s1")
        self.assertIn("Smart Falcon", out[0].text)
        self.assertIn("Verdict", out[0].text)
        self.assertEqual(out[0].meta["tools"], ["career_review"])
        # the vision call is exact-model (no text-only fallback) and asks for JSON
        self.assertEqual(len(self.provider.vision_calls), 1)
        self.assertFalse(self.provider.vision_calls[0]["fallback"])
        self.assertTrue(self.provider.vision_calls[0]["json"])

    def test_caption_picks_the_target(self):
        out = self.shot("s2", "is she good for long?")
        self.assertIn("Long Front Runner on Turf", out[0].text)
        self.assertNotIn("Mile Front Runner", out[0].text)

    def test_review_stores_nothing_about_the_user(self):
        self.shot("s3")
        self.assertEqual(self.app.memory.user.list("s3"), [])
        self.assertEqual(self.app.memory.conversation.count("s3"), 0)

    def test_screenshots_are_rate_limited_like_text(self):
        outs = [self.shot("s4") for _ in range(10)]
        self.assertTrue(any("catch up" in o[0].text for o in outs))

    def test_text_messages_still_work(self):
        self.app.memory.user.add("s5", "Test user")
        out = run(self.app.router.route(IncomingMessage("s5", "tell me something", "Tester", "simulator")))
        self.assertEqual(out[0].text, "Hello from Lily, happy to help with whatever you need today.")


if __name__ == "__main__":
    unittest.main()
