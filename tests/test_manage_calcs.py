"""Manage Mode fan analytics: the sandbox script, the sandbox/local runner and the fan_analytics tool.

No network and no API keys: the sandbox is faked and runs the real script locally.

Run:  python -m unittest tests.test_manage_calcs -v
"""
import asyncio
import importlib.util
import json
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

SCRIPT = ROOT / "LilyAiGameSpace" / "sandbox_scripts" / "manage_calcs.py"
_spec = importlib.util.spec_from_file_location("manage_calcs", SCRIPT)
mc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mc)

QUOTA = 150_000_000


def member(name, monthly, tracked=14, remaining=16, club="Umakraft", tid="1", week=None, total=1_000_000_000):
    return {"name": name, "trainer_id": tid, "club": club, "total_fans": total, "today_gain": 10, "daily_gain": 20,
            "monthly_gain": monthly, "week_avg": week, "tracked_days": tracked, "remaining_days": remaining}


def calc(op, members, **extra):
    return mc.run({"op": op, "quota": QUOTA, "members": members, **extra})


class ScriptTests(unittest.TestCase):
    def test_projection_and_status_numbers(self):
        on_pace = mc.prepare(member("A", 70_000_000), QUOTA)       # 5M/day x 16 days left = exactly the quota
        self.assertEqual(on_pace["projected"], 150_000_000)
        self.assertEqual(on_pace["status"], "on pace")
        behind = mc.prepare(member("B", 42_000_000), QUOTA)        # 3M/day -> 90M, needs (150-42)M / 16 = 6.75M/day
        self.assertEqual(behind["projected"], 90_000_000)
        self.assertEqual(behind["required"], 6_750_000)
        self.assertEqual(behind["status"], "behind")
        self.assertEqual(mc.shortfall(behind), 60_000_000)

    def test_met_missed_and_no_data(self):
        self.assertEqual(mc.prepare(member("M", 150_000_000), QUOTA)["status"], "met")
        missed = mc.prepare(member("X", 100_000_000, tracked=29, remaining=0), QUOTA)
        self.assertEqual((missed["status"], mc.shortfall(missed)), ("missed", 50_000_000))
        fresh = mc.prepare(member("F", 0, tracked=0, remaining=29), QUOTA)
        self.assertEqual((fresh["status"], fresh["projected"]), ("no data", None))

    def test_behind_quota_lists_biggest_shortfall_first_with_counts(self):
        r = calc("behind_quota", [member("Fine", 80_000_000, tid="1"), member("Slow", 30_000_000, tid="2"),
                                  member("Mid", 42_000_000, tid="3"), member("Done", 151_000_000, tid="4")])
        self.assertTrue(r["ok"], r)
        text = r["text"]
        self.assertIn("4 members: 1 met, 1 on pace, 2 behind, 0 missed, 0 no data yet.", text)
        self.assertLess(text.index("Slow"), text.index("Mid"))
        self.assertNotIn("Fine:", text)

    def test_nobody_behind(self):
        self.assertIn("Nobody is behind.", calc("behind_quota", [member("Done", 151_000_000)])["text"])

    def test_pace_prefers_this_weeks_average(self):
        r = calc("pace", [member("Quiet", 70_000_000, week=2_000_000, tid="1"), member("Busy", 70_000_000, tid="2")],
                 below=4_000_000)
        self.assertIn("1 of 2 members average under 4,000,000", r["text"])
        self.assertIn("Quiet: 2,000,000/day (this week)", r["text"])
        self.assertNotIn("Busy:", r["text"])
        self.assertFalse(calc("pace", [member("A", 1)])["ok"], "below is required")

    def test_compare_by_name_and_trainer_id(self):
        members = [member("Alpha", 42_000_000, tid="111"), member("Alphabet", 10_000_000, tid="222"),
                   member("Beta", 70_000_000, tid="333")]
        r = calc("compare", members, names="Alpha, 333")           # exact name beats the substring match on Alphabet
        self.assertTrue(r["ok"], r)
        self.assertIn("Beta vs Alpha: month +28,000,000", r["text"])
        self.assertIn("(ID 333)", r["text"])

    def test_compare_errors_are_reported_not_raised(self):
        members = [member("Alpha", 1, tid="1"), member("Alphabet", 2, tid="2")]
        self.assertFalse(calc("compare", members, names="Alp, Alphabet")["ok"])       # 'Alp' is ambiguous
        self.assertFalse(calc("compare", members, names="Alpha")["ok"])               # needs two
        self.assertFalse(calc("compare", members, names="Alpha, nobody")["ok"])

    def test_name_filter_and_limit(self):
        members = [member(f"P{i}", i * 1_000_000, tid=str(i)) for i in range(1, 41)]
        r = calc("projection", members, limit=5)
        self.assertIn("...showing 5 of 40", r["text"])
        only = calc("projection", members, names="P7, 12")
        self.assertIn("for 2 members", only["text"])

    def test_club_is_shown_only_when_there_are_two(self):
        one = calc("projection", [member("A", 1)])["text"]
        self.assertNotIn("[Umakraft]", one)
        two = calc("projection", [member("A", 1), member("B", 1, club="Umakraft 2", tid="2")])["text"]
        self.assertIn("[Umakraft 2]", two)

    def test_bad_input_is_reported_not_raised(self):
        self.assertFalse(mc.run({"op": "rm -rf", "quota": QUOTA, "members": [member("A", 1)]})["ok"])
        self.assertFalse(mc.run({"op": "projection", "quota": QUOTA, "members": []})["ok"])
        self.assertFalse(mc.run({"op": "projection", "members": [member("A", 1)]})["ok"])


# ---------------------------------------------------------------------------------------------- the runner
class _FakeFS:
    def __init__(self, files):
        self.files = files

    def write(self, path, content):
        self.files[path] = content


class _Res:
    def __init__(self, stdout, exit_code=0, stderr=""):
        self.stdout, self.exit_code, self.stderr = stdout, exit_code, stderr


class _FakeSandbox:
    killed = 0

    def __init__(self):
        self.files = {}
        self.filesystem = _FakeFS(self.files)

    def exec(self, cmd, timeout_seconds=30):
        return _Res(json.dumps(mc.run(json.loads(self.files["/workspace/params.json"]))))

    def kill(self):
        type(self).killed += 1


def _runner():
    try:
        from LilyAiGameSpace import manage_runner, sandbox_runner
    except ImportError as e:   # not importable in this environment (a missing optional dependency)
        raise unittest.SkipTest(f"runner not importable here: {e}")
    sandbox_runner._cache.clear()
    return manage_runner, sandbox_runner


class RunnerTests(unittest.TestCase):
    PARAMS = {"op": "projection", "quota": QUOTA, "members": [member("A", 42_000_000)]}

    def test_runs_in_the_sandbox_and_always_kills_it(self):
        mr, _ = _runner()
        before = _FakeSandbox.killed
        text, in_sandbox = mr.run_manage(self.PARAMS, sandbox_factory=lambda template, ttl, key: _FakeSandbox())
        self.assertTrue(in_sandbox)
        self.assertIn("projected 90,000,000", text)
        self.assertEqual(_FakeSandbox.killed, before + 1)

    def test_falls_back_to_the_same_script_when_the_sandbox_is_down(self):
        mr, _ = _runner()

        def broken(template, ttl, key):
            raise ConnectionError("no route")

        text, in_sandbox = mr.run_manage(self.PARAMS, sandbox_factory=broken)
        self.assertFalse(in_sandbox)
        self.assertIn("projected 90,000,000", text)

    def test_a_bad_parameter_is_an_error_not_a_silent_fallback(self):
        mr, sr = _runner()
        with self.assertRaises(sr.SandboxError):
            mr.run_manage({**self.PARAMS, "op": "nope"}, sandbox_factory=lambda t, ttl, k: _FakeSandbox())


# ---------------------------------------------------------------------------------------------- the tool
class _FakeClient:
    def __init__(self, circles):
        self.circles = circles

    async def get_circle(self, circle_id):
        return self.circles[circle_id]


def _daily(start, step, days, month_len=30):
    """Cumulative totals for `days` days, then 0 padding for the days that haven't happened (like uma.moe)."""
    return [start + step * i for i in range(days)] + [0] * (month_len - days)


class ToolTests(unittest.TestCase):
    def setUp(self):
        # never reach a real sandbox from a test, even on a machine that has a PandaStack key set
        patcher = mock.patch.dict(os.environ, {"PANDASTACK_API_KEY": ""})
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_day_counts(self):
        from LilyAiTool.ManageTools.fan_analytics import day_counts
        self.assertEqual(day_counts(_daily(1_000, 5, 14)), (13, 16))
        self.assertEqual(day_counts([0] * 10 + [5, 6, 7] + [0] * 17), (2, 17))   # joined mid-month
        self.assertEqual(day_counts([0] * 30), (0, 29))
        self.assertEqual(day_counts(None), (0, 0))

    def test_tool_projects_the_whole_roster_and_sends_no_discord_ids(self):
        _runner()
        from LilyAiTool.ManageTools import fan_analytics_tools
        from LilyAiTool.Models.tool_models import ToolContextData

        seen = {}
        from LilyAiGameSpace import manage_runner
        real = manage_runner.run_manage

        def spy(params, **kw):
            seen.update(params)
            return real(params, **kw)

        manage_runner.run_manage = spy
        try:
            # 14 days of data at 3,000,000 a day: monthly gain 39,000,000 over 13 steps, 16 days left -> 87,000,000
            members = [{"viewer_id": 100 + i, "trainer_name": f"T{i}", "daily_fans": _daily(1_000_000_000, 3_000_000, 14)}
                       for i in range(40)]                      # 40 members: more than check_fan_gain's top 25
            client = _FakeClient({7: {"circle": {"name": "Umakraft"}, "members": members}})
            spec = fan_analytics_tools(client, (7,), QUOTA)[0]
            out = asyncio.run(spec.handler(ToolContextData("discord-123", "Tester"), {"op": "projection", "limit": 30}))
        finally:
            manage_runner.run_manage = real
        self.assertEqual(spec.category, "umamoe")
        self.assertEqual(len(seen["members"]), 40)
        self.assertIn("projected 87,000,000", out)
        self.assertNotIn("discord-123", json.dumps(seen))
        self.assertIn("calculated", out)

    def test_tool_rejects_an_unknown_op(self):
        _runner()
        from LilyAiCore.Exceptions.errors import ToolError
        from LilyAiTool.ManageTools import fan_analytics_tools
        from LilyAiTool.Models.tool_models import ToolContextData

        spec = fan_analytics_tools(_FakeClient({}), (7,), QUOTA)[0]
        with self.assertRaises(ToolError):
            asyncio.run(spec.handler(ToolContextData(), {"op": "drop tables"}))


if __name__ == "__main__":
    unittest.main()
