"""Regression tests for the Deficit task bugs fixed alongside this file:

1. month rollover: last month's carry/total must not leak into the new month, even
   though the 1st is a first_tracked_day for everyone (so the quota path is skipped)
   and even if the job never ran on the 1st
2. re-running the job on the same UTC day must not charge that day twice
3. "Required today" must never show a negative number
4. one member's failed DM must not stop everyone after them
5. one malformed trainer link must not hide every other linked member

Run:  python -m unittest discover -s tests -v
"""
import asyncio
import sys
import types
import unittest
from calendar import timegm
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.modules.setdefault("discord", types.SimpleNamespace(Client=object))

from LilyAiTask.DailyTask.DeficitTask.Deficit import (  # noqa: E402
    format_daily_message,
    linked_members,
    send_daily_dm,
    LinkedMember,
)
from LilyAiTask.DailyTask.DeficitTask.snapshot_job import run_daily_fan_gain  # noqa: E402


def _ts(dt):
    return float(timegm(dt.timetuple()))


class FakeUmamoe:
    def __init__(self, members):
        self._members = members

    async def get_circle(self, circle_id=None):
        return {"members": self._members}


class FakeLinks:
    def __init__(self, links):
        self._links = links

    def all_linked(self):
        return self._links


class FakeFanStore:
    def record(self, club, trainer_id, fan_total):
        pass


class FakeState:
    def __init__(self, carry, total_gained, updated_at):
        self.carry, self.total_gained, self.updated_at = carry, total_gained, updated_at


class FakeStateStore:
    """Stamps updated_at from `clock`, like the real store stamps now_ts()."""

    def __init__(self):
        self.clock = None
        self.saved = {}
        self.set_calls = []
        self.reset_calls = []

    def get(self, club, trainer_id):
        return self.saved.get((club, trainer_id))

    def set(self, club, trainer_id, carry, total_gained):
        self.saved[(club, trainer_id)] = FakeState(carry, total_gained, _ts(self.clock))
        self.set_calls.append((club, trainer_id, carry, total_gained))

    def reset(self, club, trainer_id):
        self.saved[(club, trainer_id)] = FakeState(0, 0, _ts(self.clock))
        self.reset_calls.append((club, trainer_id))


class FakeUser:
    def __init__(self, sink, discord_id):
        self.sink, self.discord_id = sink, discord_id

    async def send(self, message):
        self.sink.append((self.discord_id, message))


class FakeClient:
    def __init__(self, fail_ids=()):
        self.sent = []
        self.fail_ids = set(fail_ids)

    def get_user(self, discord_id):
        return None if discord_id in self.fail_ids else FakeUser(self.sent, discord_id)

    async def fetch_user(self, discord_id):
        raise RuntimeError("Cannot send messages to this user")  # like discord.Forbidden


def _link(discord_id, trainer_id, name):
    return types.SimpleNamespace(discord_id=discord_id, trainer_id=trainer_id, trainer_name=name)


def _run(coro):
    return asyncio.new_event_loop().run_until_complete(coro)


def _day(store, client, members, links, now):
    store.clock = now
    _run(run_daily_fan_gain(client, FakeLinks(links), FakeFanStore(), store,
                            FakeUmamoe(members), circle_id=1, club="Umakraft", now=now))


class MonthRolloverTests(unittest.TestCase):
    def test_first_of_month_clears_last_months_state_even_though_quota_path_is_skipped(self):
        store, client = FakeStateStore(), FakeClient()
        store.saved[("Umakraft", "3")] = FakeState(2_000_000, 140_000_000, _ts(datetime(2026, 10, 31, 20)))
        links = [_link(333, "3", "A")]

        # Nov 1: array has exactly one data point -> first_tracked_day -> no DM / no quota
        _day(store, client, [{"viewer_id": 3, "daily_fans": [50_000_000] + [0] * 29}], links, datetime(2026, 11, 1, 9))
        self.assertEqual(store.reset_calls, [("Umakraft", "3")])
        self.assertEqual(client.sent, [])

        # Nov 2: gained 2m against a clean 5m requirement -> carry 3m, not 5m (2m old + 5m - 2m)
        _day(store, client, [{"viewer_id": 3, "daily_fans": [50_000_000, 52_000_000] + [0] * 28}],
             links, datetime(2026, 11, 2, 9))
        self.assertEqual(store.set_calls, [("Umakraft", "3", 3_000_000, 2_000_000)])

    def test_stale_state_dropped_even_if_the_first_was_never_polled(self):
        store, client = FakeStateStore(), FakeClient()
        store.saved[("Umakraft", "3")] = FakeState(2_000_000, 140_000_000, _ts(datetime(2026, 10, 31, 20)))
        links = [_link(333, "3", "A")]

        _day(store, client, [{"viewer_id": 3, "daily_fans": [50_000_000, 51_000_000, 54_000_000] + [0] * 28}],
             links, datetime(2026, 11, 3, 9))
        self.assertEqual(store.reset_calls, [("Umakraft", "3")])
        # gained 3m vs clean 5m -> carry 2m, total 3m
        self.assertEqual(store.set_calls, [("Umakraft", "3", 2_000_000, 3_000_000)])

    def test_same_month_state_is_kept(self):
        store, client = FakeStateStore(), FakeClient()
        store.saved[("Umakraft", "3")] = FakeState(2_000_000, 10_000_000, _ts(datetime(2026, 11, 4, 9)))
        links = [_link(333, "3", "A")]

        _day(store, client, [{"viewer_id": 3, "daily_fans": [50_000_000, 51_000_000, 54_000_000, 57_000_000] + [0] * 27}],
             links, datetime(2026, 11, 5, 9))
        self.assertEqual(store.reset_calls, [])
        # required 5m + 2m owed = 7m, gained 3m -> carry 4m
        self.assertEqual(store.set_calls, [("Umakraft", "3", 4_000_000, 13_000_000)])


class IdempotencyTests(unittest.TestCase):
    def test_rerun_same_utc_day_does_not_double_charge(self):
        store, client = FakeStateStore(), FakeClient()
        members = [{"viewer_id": 2, "daily_fans": [10_000_000, 13_000_000] + [0] * 29}]
        links = [_link(222, "2", "V")]

        _day(store, client, members, links, datetime(2026, 9, 15, 6))
        _day(store, client, members, links, datetime(2026, 9, 15, 18))  # redeploy re-run

        self.assertEqual(store.set_calls, [("Umakraft", "2", 2_000_000, 3_000_000)])
        self.assertEqual(len(client.sent), 1)

    def test_next_day_still_counts(self):
        store, client = FakeStateStore(), FakeClient()
        links = [_link(222, "2", "V")]
        _day(store, client, [{"viewer_id": 2, "daily_fans": [10_000_000, 13_000_000] + [0] * 29}],
             links, datetime(2026, 9, 15, 6))
        _day(store, client, [{"viewer_id": 2, "daily_fans": [10_000_000, 13_000_000, 21_000_000] + [0] * 28}],
             links, datetime(2026, 9, 16, 6))
        # day 2: required 5m + 2m owed = 7m, gained 8m -> surplus 1m
        self.assertEqual(store.set_calls[-1], ("Umakraft", "2", -1_000_000, 11_000_000))
        self.assertEqual(len(client.sent), 2)


class MessageTests(unittest.TestCase):
    def test_required_today_never_negative(self):
        result = {"required": -2_000_000, "gained": 0, "met": True, "carry": -2_000_000, "total_gained": 0}
        msg = format_daily_message(result)
        self.assertIn("Required today: 0", msg)
        self.assertNotIn("-2,000,000", msg.split("Status")[0])
        self.assertIn("Surplus of 2,000,000", msg)

    def test_normal_required_unchanged(self):
        result = {"required": 7_000_000, "gained": 3_000_000, "met": False, "carry": 4_000_000, "total_gained": 3_000_000}
        self.assertIn("Required today: 7,000,000", format_daily_message(result))


class FailureIsolationTests(unittest.TestCase):
    def test_failed_dm_does_not_abort_later_members(self):
        store, client = FakeStateStore(), FakeClient(fail_ids={111})
        members = [
            {"viewer_id": 1, "daily_fans": [10_000_000, 16_000_000] + [0] * 29},
            {"viewer_id": 2, "daily_fans": [10_000_000, 15_000_000] + [0] * 29},
        ]
        links = [_link(111, "1", "ClosedDMs"), _link(222, "2", "Open")]

        _day(store, client, members, links, datetime(2026, 9, 15, 6))

        self.assertEqual([d for d, _ in client.sent], [222])       # second member still got theirs
        self.assertEqual(len(store.set_calls), 2)                   # both trainers' state saved

    def test_send_daily_dm_swallows_send_errors(self):
        member = LinkedMember(discord_id=111, trainer_id="1", trainer_name="X")
        result = {"required": 5, "gained": 5, "met": True, "carry": 0, "total_gained": 5}
        _run(send_daily_dm(FakeClient(fail_ids={111}), member, result))  # must not raise

    def test_malformed_link_row_is_skipped(self):
        links = [_link("not-a-number", "9", "Bad"), _link(222, "2", "Good")]
        members = linked_members(FakeLinks(links))
        self.assertEqual([m.trainer_id for m in members], ["2"])


if __name__ == "__main__":
    unittest.main()
