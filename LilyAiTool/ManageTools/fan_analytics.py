"""Groq tool for Manage Mode: quota / projection / pace / compare over the WHOLE roster (check_fan_gain stops at 25).

The numbers per member come from member_gains() (LilyAiCore/ExternalServices/Umamoe/gains.py), the one implementation of
the fan-gain maths. The comparison with the quota and the month projection run in a fixed script inside a PandaStack
sandbox (LilyAiGameSpace/sandbox_scripts/manage_calcs.py), or locally if the sandbox is unavailable. The model only picks
an operation and its parameters, so it never does the arithmetic itself.

Only trainer name, Trainer ID, club and fan numbers are sent. Never a Discord ID.
"""
from __future__ import annotations

from typing import Any

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiCore.ExternalServices.Umamoe.gains import member_gains
from LilyAiGameSpace import manage_runner
from LilyAiGameSpace.sandbox_runner import SandboxError
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec

CATEGORY = "umamoe"
OPS = ("behind_quota", "projection", "pace", "compare")


def day_counts(daily_fans: list | None) -> tuple[int, int]:
    """(tracked_days, remaining_days) for one member: the day-to-day steps already inside monthly_gain, and the steps still
    to come this month. Counts days only. The fan numbers themselves always come from member_gains().

    daily_fans is a full calendar month of cumulative totals with 0 padding for days that haven't happened yet, so the last
    non-zero entry is the latest day and the first non-zero entry is where this trainer's tracking starts.
    """
    daily = daily_fans or []
    live = [i for i, v in enumerate(daily) if isinstance(v, (int, float)) and not isinstance(v, bool) and v]
    if not live:
        return 0, max(0, len(daily) - 1)
    return live[-1] - live[0], len(daily) - 1 - live[-1]


def _opt(args: dict, key: str) -> Any:
    value = args.get(key)
    if isinstance(value, str):
        value = value.strip()
    return value if value not in (None, "") else None


def fan_analytics_tools(client: Any, default_circle_ids: tuple[int, ...], quota: int) -> list[ToolSpec]:
    async def fan_analytics(ctx: ToolContextData, args: dict) -> str:
        op = str(_opt(args, "op") or "").lower()
        if op not in OPS:
            raise ToolError(f"op must be one of: {', '.join(OPS)}")
        circle_id = _opt(args, "circle_id")
        ids = (circle_id,) if circle_id else default_circle_ids
        if not ids:
            return "No uma.moe circle configured. Set UMAMOE_CIRCLE_IDS or pass a circle_id."
        members: list[dict] = []
        for cid in ids:
            data = await client.get_circle(circle_id=cid)
            club = (data.get("circle") or {}).get("name") or str(cid)
            for m in data.get("members", []):
                daily = m.get("daily_fans") or []
                if not daily:
                    continue
                gains = member_gains(daily)
                tracked, remaining = day_counts(daily)
                members.append({
                    "name": m.get("trainer_name") or str(m.get("viewer_id") or ""),
                    "trainer_id": str(m.get("viewer_id") or ""),
                    "club": club,
                    "total_fans": gains["total_fans"], "today_gain": gains["today_gain"],
                    "daily_gain": gains["daily_gain"], "monthly_gain": gains["monthly_gain"],
                    "week_avg": gains["week_avg"], "tracked_days": tracked, "remaining_days": remaining,
                })
        if not members:
            return "No members with fan data found."
        params: dict[str, Any] = {"op": op, "quota": quota, "members": members}
        for key, source in (("names", "trainer_names"), ("below", "below"), ("limit", "limit")):
            if _opt(args, source) is not None:
                params[key] = _opt(args, source)
        try:
            text, in_sandbox = await manage_runner.run_manage_async(params)
        except SandboxError as e:
            raise ToolError(str(e))
        where = "in a PandaStack sandbox" if in_sandbox else "locally (the sandbox wasn't available)"
        return f"Fan analytics from uma.moe daily fan data, calculated {where}. Quote the numbers exactly:\n{text}"

    return [
        ToolSpec(
            "fan_analytics",
            "Monthly-quota and pace analysis over the WHOLE roster of the tracked club(s), calculated exactly: "
            "op='behind_quota' = who is behind or missed the monthly fan-gain quota, with the fans per day they still need; "
            "op='projection' = projected month-end gain per trainer (straight line); op='pace' = who averages under "
            "`below` fans per day; op='compare' = two or more trainers side by side (trainer_names, 2+). "
            "Use it for 'who is behind on quota', 'can I still make quota', 'projected month end', 'who is under X a day'. "
            "Use check_fan_gain for a plain leaderboard or one trainer's current numbers. Never do this arithmetic "
            "yourself and quote the numbers exactly. For 'my' numbers resolve the Trainer ID with get_linked_trainer "
            "first and pass it in trainer_names.",
            {"type": "object", "properties": {
                "op": {"type": "string", "enum": list(OPS),
                       "description": "behind_quota, projection, pace or compare"},
                "trainer_names": {"type": ["string", "null"],
                                  "description": "Comma-separated names or numeric Trainer IDs. Filters behind_quota, "
                                                 "projection and pace; required (2+) for compare"},
                "below": {"type": ["number", "null"], "description": "pace only: fans per day threshold"},
                "limit": {"type": ["integer", "null"], "description": "Rows to show (default 15, max 30)"},
                "circle_id": {"type": ["integer", "null"], "description": "Omit or pass null for the default club(s)"},
            }, "required": ["op"]},
            fan_analytics, category=CATEGORY, timeout=60.0,
        ),
    ]
