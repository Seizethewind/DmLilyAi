"""Daily fan snapshot + quota job.

Wires the Deficit flow up to real uma.moe data: for every linked trainer in a
club, reads today's and this month's fan gain straight from uma.moe's own
daily_fans array (via LilyAiCore.ExternalServices.Umamoe.gains.member_gains -
the exact same calculation /api/leaderboard uses) and feeds today's gain into
the DeficitTracker that drives the quota DM.

Gains used to be computed by diffing our own LilyAiMemory.FanGain.FanSnapshotStore
snapshots day over day. That was broken: a trainer's very first tracked day (no
previous local snapshot to diff against) and any run right after a Render
redeploy (the free-plan filesystem is ephemeral, so "yesterday's" row is gone -
see .env.example's TURSO note) both silently came back as "0 gained, 0 /
150,000,000 monthly" regardless of the trainer's real activity, because there
was nothing to diff against. uma.moe's daily_fans array already hands back a
full calendar month of cumulative snapshots in one get_circle() call, so
reading gains from it directly needs no local history and can't cold-start to
zero.

FanSnapshotStore is still written here as a historical record of each day's
total_fans (harmless, and useful if that log is ever wanted later), but it no
longer participates in the gain math.

DeficitTracker's own carry (deficit owed / surplus banked toward the monthly
quota) is a different kind of state - it can't be recomputed from uma.moe on
demand, it only exists because of what record_day() was called with on past
days. That state is persisted via LilyAiMemory.DeficitState.DeficitStateStore
(loaded at the top of each trainer's turn below, saved back right after
record_day()), so a process restart or Render redeploy carries it over
instead of silently zeroing a trainer's carry.

Two guards keep that persisted state honest:
- Month boundary: state saved in an earlier calendar month (judged by the
  store's updated_at) is reset before anything else happens, even on a day
  that is itself skipped as a first_tracked_day, and even if the job missed
  the 1st entirely. Otherwise last month's deficit leaks into the new month.
- One quota day per trainer per UTC day: if this trainer's state was already
  written today, a re-run (redeploy mid-day, manual trigger) skips them
  instead of calling record_day() a second time and double-charging the day.

There is no scraper here: fan data comes from the existing UmamoeClient (the
same client that already powers check_umamoe and /api/leaderboard, configured
via UMAMOE_API_KEY / UMAMOE_CIRCLE_IDS - see render.yaml and .env.example).
One get_circle(circle_id) call per run returns every tracked member's
daily_fans in one shot, the same call umamoe_job.py already makes for the
rank/points poll.
"""
from __future__ import annotations

from datetime import datetime, timezone

import discord

from LilyAiCore.ExternalServices.Umamoe.client import UmamoeClient
from LilyAiCore.ExternalServices.Umamoe.gains import member_gains
from LilyAiMemory.DeficitState.deficit_state_store import DeficitStateStore
from LilyAiMemory.FanGain.fan_gain import FanSnapshotStore
from LilyAiMemory.TrainerLink.trainer_link import TrainerLinkStore
from LilyAiTask.DailyTask.DeficitTask.Deficit import (
    DeficitTracker,
    linked_members,
    send_daily_dm,
)


def _is_first_of_month(now: datetime) -> bool:
    return now.day == 1


def _saved_at(saved) -> datetime | None:
    """When a saved DeficitState was last written (UTC), or None if the store
    doesn't expose updated_at."""
    ts = getattr(saved, "updated_at", None)
    if ts is None:
        return None
    return datetime.fromtimestamp(float(ts), tz=timezone.utc)


def _is_stale_state(saved, now: datetime) -> bool:
    """True when saved carry/total_gained belongs to an earlier month and must
    not be carried into this one. Falls back to "is today the 1st?" when the
    saved record has no updated_at."""
    saved_at = _saved_at(saved)
    if saved_at is None:
        return _is_first_of_month(now)
    return (saved_at.year, saved_at.month) != (now.year, now.month)


def _already_ran_today(saved, now: datetime) -> bool:
    """True when this trainer's quota state was already written today (UTC)."""
    saved_at = _saved_at(saved)
    return saved_at is not None and saved_at.date() == now.date()


async def _fetch_member_gains(umamoe: UmamoeClient, circle_id: int) -> dict[str, dict]:
    """trainer_id (uma.moe viewer_id, as str) -> member_gains() breakdown
    (total_fans/today_gain/daily_gain/monthly_gain/week_avg/first_tracked_day) for
    every member currently on this circle's live roster.
    """
    data = await umamoe.get_circle(circle_id=circle_id)
    out: dict[str, dict] = {}
    for member in data.get("members", []):
        viewer_id = member.get("viewer_id")
        if viewer_id is None:
            continue
        out[str(viewer_id)] = member_gains(member.get("daily_fans"))
    return out


def _load_tracker(tracker_store: DeficitStateStore, club: str, trainer_id: str, now: datetime) -> DeficitTracker:
    """Rebuild a trainer's DeficitTracker from its last saved carry/total_gained,
    or start fresh if nothing's been saved for them yet or what's saved is from an
    earlier month (a new tally period)."""
    saved = tracker_store.get(club, trainer_id)
    if saved is None or _is_stale_state(saved, now):
        return DeficitTracker()
    return DeficitTracker(carry=saved.carry, total_gained=saved.total_gained)


async def run_daily_fan_gain(
    client: discord.Client,
    trainer_link_store: TrainerLinkStore,
    fan_store: FanSnapshotStore,
    tracker_store: DeficitStateStore,
    umamoe: UmamoeClient,
    circle_id: int,
    club: str,
    now: datetime | None = None,
) -> None:
    """Run one day's quota cycle for every linked trainer in `club`.

    Args:
        client: logged-in discord.Client/Bot, passed through to send_daily_dm.
        trainer_link_store: source of linked Discord<->trainer pairs.
        fan_store: FanSnapshotStore - written here purely as a historical log
            of each day's total_fans; today_gain/monthly_gain both come from
            member_gains() below, not from diffing these snapshots.
        tracker_store: DeficitStateStore - persists each trainer's DeficitTracker
            carry/total_gained across runs and process restarts (e.g.
            app.memory.deficit_state).
        umamoe: the shared UmamoeClient (app.umamoe - None means
            UMAMOE_API_KEY isn't set, in which case this job shouldn't be
            scheduled; see bootstrap.py).
        circle_id: the uma.moe circle id this club maps to (one of
            settings.umamoe_circle_ids).
        club: which club this run is for ("Umakraft" / "Umakraft 2").
        now: override for testing; defaults to current UTC time.
    """
    now = now or datetime.now(timezone.utc)
    members = linked_members(trainer_link_store)
    if not members:
        return

    member_gain_data = await _fetch_member_gains(umamoe, circle_id)

    for member in members:
        gains = member_gain_data.get(member.trainer_id)
        if gains is None:
            # Linked trainer isn't on this circle's live roster right now
            # (e.g. dropped from the club) - nothing to report today.
            continue

        fan_store.record(club, member.trainer_id, gains["total_fans"])

        # Month boundary first, before any skip below: on the 1st every trainer is a
        # first_tracked_day, so resetting only inside the quota path (as this used to)
        # meant the reset never ran and last month's carry leaked into day 2.
        saved = tracker_store.get(club, member.trainer_id)
        if saved is not None and _is_stale_state(saved, now):
            tracker_store.reset(club, member.trainer_id)
            saved = None

        if gains["first_tracked_day"]:
            # No earlier day of data to measure "today" against yet - either uma.moe just
            # detected this trainer (mid-month join) or this is the first poll of a new
            # tracking month for everyone. member_gains() already forces today_gain to 0 in
            # this case (see gains.py), but feeding that 0 into record_day() would still
            # charge the full 5,000,000 daily quota as a deficit against someone who hasn't
            # had a chance to gain anything measurable yet. Skip quota tracking and the DM
            # for this one day; tomorrow's _load_tracker() starts from a clean carry=0
            # instead of an artificial deficit.
            continue

        if saved is not None and _already_ran_today(saved, now):
            # Already counted today (re-run after a redeploy / manual trigger). Calling
            # record_day() again would add today's shortfall to the carry a second time.
            continue

        tracker = _load_tracker(tracker_store, club, member.trainer_id, now)
        result = tracker.record_day(gains["today_gain"])
        tracker_store.set(club, member.trainer_id, tracker.carry, tracker.total_gained)

        await send_daily_dm(client, member, result, monthly_gain=gains["monthly_gain"])
