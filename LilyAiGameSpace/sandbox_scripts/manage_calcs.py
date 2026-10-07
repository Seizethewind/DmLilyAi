"""Manage Mode fan analytics. Runs INSIDE a PandaStack sandbox (or locally, see LilyAiGameSpace/manage_runner.py).
Standard library only.

LilyAi uploads /workspace/params.json and runs this file. It prints one JSON object:
{"ok": true, "text": "..."} or {"ok": false, "error": "..."}. The model only supplies parameters, never code.

This script does NOT work out fan gains. Every member arrives with gains LilyAi already computed with
LilyAiCore/ExternalServices/Umamoe/gains.py (the one implementation of that maths), so the leaderboard, the daily quota DM
and this tool can never disagree. The script only compares them with the quota and projects the month.

params = {
    "op": "behind_quota" | "projection" | "pace" | "compare",
    "quota": 150000000,
    "members": [{"name", "trainer_id", "club", "total_fans", "today_gain", "daily_gain", "monthly_gain",
                 "week_avg", "tracked_days", "remaining_days"}],
    "names": "comma separated names or Trainer IDs",   # optional filter; compare needs 2 or more
    "below": 4000000,                                   # pace: list members averaging under this many fans per day
    "limit": 15,
}

tracked_days   = day-to-day steps already inside monthly_gain; remaining_days = steps still to come this month.
Projection is a straight line: monthly_gain + (monthly_gain / tracked_days) * remaining_days.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARAMS = Path("/workspace/params.json")
OPS = ("behind_quota", "projection", "pace", "compare")
DEFAULT_LIMIT, MAX_LIMIT, MAX_MEMBERS = 15, 30, 200


class CalcError(Exception):
    pass


# ----------------------------------------------------------------------------- helpers
def num(v: float) -> str:
    return f"{int(round(v)):,}"


def as_number(x, name, lo=None) -> float:
    if x is None or x == "" or isinstance(x, bool):
        raise CalcError(f"{name} is required and must be a number")
    try:
        v = float(str(x).replace(",", "").strip())
    except ValueError:
        raise CalcError(f"{name} must be a number, got {x!r}")
    if lo is not None and v < lo:
        raise CalcError(f"{name} must be at least {lo:g}")
    return v


def whole(x, default: int = 0) -> int:
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def prepare(raw: dict, quota: int) -> dict:
    """One member's numbers against the quota. Pure arithmetic on gains that were computed elsewhere."""
    monthly = whole(raw.get("monthly_gain"))
    tracked = max(0, whole(raw.get("tracked_days")))
    remaining = max(0, whole(raw.get("remaining_days")))
    avg = monthly / tracked if tracked > 0 else None
    projected = round(monthly + avg * remaining) if avg is not None else None
    need = max(0, quota - monthly)
    if monthly >= quota:
        status, required = "met", 0.0
    elif remaining == 0:
        status, required = "missed", None
    else:
        required = need / remaining
        status = "no data" if avg is None else ("on pace" if projected >= quota else "behind")
    week = raw.get("week_avg")
    week = whole(week) if isinstance(week, (int, float)) and not isinstance(week, bool) else None
    pace, basis = (week, "this week") if week is not None else (avg, "this month")
    tid = str(raw.get("trainer_id") or "")
    return {
        "name": str(raw.get("name") or tid or "?"), "id": tid, "club": str(raw.get("club") or ""),
        "total": whole(raw.get("total_fans")), "today": whole(raw.get("today_gain")),
        "yesterday": whole(raw.get("daily_gain")), "monthly": monthly, "avg": avg, "projected": projected,
        "need": need, "required": required, "status": status, "pace": pace, "basis": basis, "quota": quota,
    }


def shortfall(m: dict) -> int:
    if m["status"] == "missed":
        return m["need"]
    if m["status"] == "behind":
        return m["quota"] - m["projected"]
    return 0


def detail(m: dict) -> str:
    bits = [f"{num(m['monthly'])} this month"]
    if m["avg"] is not None:
        bits.append(f"avg {num(m['avg'])}/day")
    if m["projected"] is not None:
        bits.append(f"projected {num(m['projected'])}")
    if m["status"] in ("behind", "on pace", "no data") and m["required"] is not None:
        bits.append(f"needs {num(m['required'])}/day")
    verdict = {
        "met": "MET", "on pace": "on pace", "no data": "no data yet",
        "behind": f"BEHIND, about {num(shortfall(m))} short",
        "missed": f"MISSED by {num(m['need'])}",
    }[m["status"]]
    return ", ".join(bits) + f" - {verdict}"


def who(m: dict, multi_club: bool) -> str:
    return m["name"] + (f" [{m['club']}]" if multi_club and m["club"] else "")


def tokens_of(names) -> list[str]:
    items = names if isinstance(names, list) else str(names or "").split(",")
    return [str(t).strip() for t in items if str(t).strip()]


def token_matches(token: str, m: dict) -> bool:
    digits = token.replace(" ", "").replace(",", "")
    if digits.isdigit():                      # a Trainer ID
        return m["id"] == digits
    return token.lower() in m["name"].lower()


def resolve_one(token: str, pool: list[dict]) -> dict:
    hits = [m for m in pool if token_matches(token, m)]
    if len(hits) > 1:
        exact = [m for m in hits if m["name"].lower() == token.lower()]
        if len(exact) == 1:
            return exact[0]
        raise CalcError(f"{token!r} matches {len(hits)} members ({', '.join(m['name'] for m in hits[:5])}). "
                        "Use the full name or the Trainer ID.")
    if not hits:
        raise CalcError(f"No member matches {token!r}.")
    return hits[0]


# ----------------------------------------------------------------------------- operations
def op_behind_quota(pool, limit, multi, params) -> str:
    counts = {k: sum(1 for m in pool if m["status"] == k) for k in ("met", "on pace", "behind", "missed", "no data")}
    head = (f"{len(pool)} members: {counts['met']} met, {counts['on pace']} on pace, {counts['behind']} behind, "
            f"{counts['missed']} missed, {counts['no data']} no data yet.")
    rows = sorted((m for m in pool if m["status"] in ("behind", "missed")), key=lambda m: (-shortfall(m), m["name"].lower()))
    if not rows:
        return head + "\nNobody is behind."
    lines = [f"{i}. {who(m, multi)}: {detail(m)}" for i, m in enumerate(rows[:limit], 1)]
    more = f"\n...showing {limit} of {len(rows)}; filter by name for the rest." if len(rows) > limit else ""
    return head + "\nBehind or missed, biggest shortfall first:\n" + "\n".join(lines) + more


def op_projection(pool, limit, multi, params) -> str:
    rows = sorted(pool, key=lambda m: (m["projected"] is None, -(m["projected"] or 0), m["name"].lower()))
    lines = [f"{i}. {who(m, multi)}: {detail(m)}" for i, m in enumerate(rows[:limit], 1)]
    more = f"\n...showing {limit} of {len(rows)}; filter by name for the rest." if len(rows) > limit else ""
    return f"Projected month-end fan gain for {len(rows)} members, highest first:\n" + "\n".join(lines) + more


def op_pace(pool, limit, multi, params) -> str:
    below = as_number(params.get("below"), "below (fans per day)", 0)
    known = [m for m in pool if m["pace"] is not None]
    under = sorted((m for m in known if m["pace"] < below), key=lambda m: (m["pace"], m["name"].lower()))
    nodata = f" ({len(pool) - len(known)} have no pace data yet)" if len(known) < len(pool) else ""
    head = (f"{len(under)} of {len(known)} members average under {num(below)} fans/day{nodata}. "
            "Pace = this week's average per day, else the month's.")
    if not under:
        return head
    lines = [f"{i}. {who(m, multi)}: {num(m['pace'])}/day ({m['basis']}), {num(m['monthly'])} this month"
             for i, m in enumerate(under[:limit], 1)]
    more = f"\n...showing {limit} of {len(under)}; filter by name for the rest." if len(under) > limit else ""
    return head + "\n" + "\n".join(lines) + more


def op_compare(pool, limit, multi, params) -> str:
    tokens = tokens_of(params.get("names"))
    if len(tokens) < 2:
        raise CalcError("compare needs at least two names or Trainer IDs in names")
    rows: list[dict] = []
    for t in tokens[:6]:
        m = resolve_one(t, pool)
        if all(m is not r for r in rows):
            rows.append(m)
    if len(rows) < 2:
        raise CalcError("those names all point at the same member; give two different trainers")
    out = []
    for m in rows:
        out.append(f"- {who(m, multi)} (ID {m['id']}): today {num(m['today'])}, yesterday {num(m['yesterday'])}, "
                   f"month {num(m['monthly'])}, total {num(m['total'])}\n    {detail(m)}")
    first = rows[0]
    for m in rows[1:]:
        out.append(f"{m['name']} vs {first['name']}: month {m['monthly'] - first['monthly']:+,}, "
                   f"total {m['total'] - first['total']:+,}")
    return "\n".join(out)


HANDLERS = {"behind_quota": op_behind_quota, "projection": op_projection, "pace": op_pace, "compare": op_compare}


def run(params: dict) -> dict:
    op = str(params.get("op") or "").strip().lower()
    if op not in OPS:
        return {"ok": False, "error": f"op must be one of: {', '.join(OPS)}"}
    try:
        quota = int(as_number(params.get("quota"), "quota", 1))
        raw = params.get("members")
        if not isinstance(raw, list) or not raw:
            raise CalcError("members must be a non-empty list")
        if len(raw) > MAX_MEMBERS:
            raise CalcError(f"too many members ({len(raw)}); the limit is {MAX_MEMBERS}")
        everyone = [prepare(m, quota) for m in raw if isinstance(m, dict)]
        if not everyone:
            raise CalcError("members must be a list of objects")
        multi = len({m["club"] for m in everyone if m["club"]}) > 1
        limit = DEFAULT_LIMIT
        if params.get("limit") not in (None, ""):
            limit = int(min(MAX_LIMIT, as_number(params.get("limit"), "limit", 1)))
        pool = everyone
        tokens = tokens_of(params.get("names"))
        if op != "compare" and tokens:
            pool = [m for m in everyone if any(token_matches(t, m) for t in tokens)]
            if not pool:
                raise CalcError("No member matches: " + ", ".join(tokens))
        body = HANDLERS[op](everyone if op == "compare" else pool, limit, multi, params)
    except CalcError as e:
        return {"ok": False, "error": str(e)}
    head = (f"Quota {num(quota)} fans per month. Projection = fans gained so far / days counted x days left (straight "
            "line; today counts as a full day, so it errs low early in the day).")
    return {"ok": True, "text": head + "\n" + body}


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        result = run(params if isinstance(params, dict) else {})
    except Exception as e:
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
