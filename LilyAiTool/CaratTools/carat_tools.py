"""Manage Mode tools for the carat tracker: the user says their current carat balance, the bot works out the gain.

Gain = new balance - last balance. A drop is never recorded silently: the tool refuses it and tells the model to ask
the user what happened (pulls, another expense, or a wrong number), then the model calls again with the answer.
All reads and writes are for ctx.user_id only.
"""
from __future__ import annotations

from datetime import datetime, timezone

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiMemory.Carat.carat_store import CARATS_PER_PULL, CaratError, CaratStore, classify
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec

CATEGORY = "carats"
BIG_JUMP = 20000   # one entry gaining more than this is worth a "was that right?" in the reply


def _int(args: dict, key: str, required: bool = False) -> int | None:
    v = args.get(key)
    if v in (None, ""):
        if required:
            raise ToolError(f"{key} is required.")
        return None
    if isinstance(v, bool):
        raise ToolError(f"{key} must be a number.")
    try:
        if isinstance(v, str):
            v = v.strip().lower().replace(",", "").replace(" ", "")
            n = float(v[:-1]) * 1000 if v.endswith("k") else float(v)
        else:
            n = float(v)
    except ValueError:
        raise ToolError(f"{key} must be a number, e.g. 18500.") from None
    if n != int(n):
        raise ToolError(f"{key} must be a whole number of carats.")
    return int(n)


def _day(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _rate(w: dict | None) -> str:
    if not w:
        return "Not enough entries yet for a daily income figure."
    return (f"Income over the last {w['days']:.1f} days: +{w['income']:,} (about {w['per_day']:,.0f} per day), "
            f"spent {w['spent']:,}.")


def carat_tools(store: CaratStore) -> list[ToolSpec]:
    def need_user(ctx: ToolContextData) -> str:
        if not ctx.user_id:
            raise ToolError("No user in this context.")
        return ctx.user_id

    def carat_update(ctx: ToolContextData, args: dict) -> str:
        uid = need_user(ctx)
        balance = _int(args, "balance", required=True)
        pulls = _int(args, "pulls")
        spent = _int(args, "spent")
        if pulls is not None:
            if pulls < 0:
                raise ToolError("pulls cannot be negative.")
            spent = (spent or 0) + pulls * CARATS_PER_PULL
        reason = (args.get("reason") or "").strip() or None
        correction = bool(args.get("correction"))
        category = (args.get("category") or "").strip().lower().replace(" ", "_") or None
        prev = store.last(uid)
        if prev and balance != prev["balance"] and not (reason or pulls is not None or correction):
            d = balance - prev["balance"]
            verb = f"went UP by {d:,}" if d > 0 else f"went DOWN by {-d:,}"
            return (f"NOT RECORDED. The balance {verb} (from {prev['balance']:,} to {balance:,}). Ask the user why before "
                    "recording: " + ("where the carats came from (login bonus, missions, event or campaign reward, gift, "
                                     "shop/purchase, or something else)" if d > 0 else
                                     f"what happened (pulls, which is {-d / CARATS_PER_PULL:g} pulls if that is all of it, "
                                     "another expense, or a wrong number to correct)") +
                    ". Then call carat_update again with their answer as reason.")
        if prev and balance < prev["balance"] and spent is None and reason and not correction:
            spent = prev["balance"] - balance   # the user explained the whole drop
        try:
            e = classify(prev["balance"] if prev else None, balance, spent, correction)
        except CaratError as err:
            return f"NOT RECORDED. {err}"
        if e["kind"] == "baseline" and prev:
            note = reason or "correction"
        else:
            note = reason
        store.add(uid, balance, e["income"], e["spent"], e["kind"], note, category=category)
        if not prev:
            return (f"Recorded the starting balance: {balance:,} carats. No gain counted yet; from the next update on, the "
                    "difference is the income.")
        gap = (store.last(uid)["ts"] - prev["ts"]) / 86400
        if e["kind"] == "baseline":
            return f"Corrected: balance is now {balance:,} (was {prev['balance']:,}). Nothing counted as income or spending."
        lines = [f"Balance {balance:,} (was {prev['balance']:,} {gap:.1f} days ago)."]
        if e["spent"]:
            lines.append(f"Spent {e['spent']:,} ({e['spent'] / CARATS_PER_PULL:g} pulls' worth)" + (f": {reason}." if reason else "."))
        lines.append(f"Income since last entry: +{e['income']:,}" + (f" from {reason}" if reason and not e["spent"] else "") + (f" (about {e['income'] / gap:,.0f} per day)." if gap >= 0.04 else "."))
        if e["income"] >= BIG_JUMP:
            lines.append("That is a large gain for one stretch: confirm it with the user in case the number was mistyped "
                         "(then carat_undo and re-enter).")
        return " ".join(lines)

    def carat_status(ctx: ToolContextData, args: dict) -> str:
        uid = need_user(ctx)
        last = store.last(uid)
        if not last:
            return "No carat balance recorded yet. Ask the user for their current carat amount and use carat_update."
        days = _int(args, "days") or 30
        recent = store.recent(uid, 5)
        cats = store.by_category(uid)
        out = [f"Current balance: {last['balance']:,} carats (as of {_day(last['ts'])}, about {last['balance'] / CARATS_PER_PULL:.1f} pulls).",
               _rate(store.window(uid, max(1, min(days, 365))))]
        if cats:
            out.append("By reason (all time): " + "; ".join(
                f"{c['category'].replace('_', ' ')} " + (f"+{c['income']:,}" if c["income"] else "") +
                (f" -{c['spent']:,}" if c["spent"] else "") for c in cats))
        out.append("Latest entries:")
        for r in recent:
            extra = f" [{r['kind']}{': ' + r['note'] if r['note'] else ''}]" if r["kind"] != "gain" else ""
            out.append(f"- {_day(r['ts'])}: {r['balance']:,} (income +{r['income']:,}, spent {r['spent']:,}){extra}")
        return "\n".join(out)

    def carat_history(ctx: ToolContextData, args: dict) -> str:
        uid = need_user(ctx)
        n = max(1, min(_int(args, "limit") or 15, 50))
        rows = store.recent(uid, n)
        if not rows:
            return "No carat entries yet."
        return "\n".join(f"#{r['id']} {_day(r['ts'])}: balance {r['balance']:,}, income +{r['income']:,}, spent {r['spent']:,}, "
                         f"{r['kind']}{': ' + r['note'] if r['note'] else ''}" for r in rows)

    def carat_undo(ctx: ToolContextData, args: dict) -> str:
        row = store.delete_last(need_user(ctx))
        if not row:
            return "Nothing to undo: no entries."
        now = store.last(ctx.user_id)
        return (f"Removed the last entry ({row['balance']:,} on {_day(row['ts'])}). "
                + (f"The balance on record is now {now['balance']:,}." if now else "No entries are left."))

    obj = lambda props, req=(): {"type": "object", "properties": props, "required": list(req)}  # noqa: E731
    return [
        ToolSpec(
            "carat_update",
            "Record the user's CURRENT in-game carat balance and work out the gain since their last entry (new minus last). "
            "Call it whenever the user states their carat amount. EVERY change needs a reason, up or down. If the result "
            "starts with NOT RECORDED, ask the user why it went up (login bonus, missions, event reward, gift, shop...) or "
            "down (pulls, another expense, a typo), then call again with their answer as reason (and category), plus "
            "pulls=<number> or spent=<carats> when they spent some, or correction=true if a number was wrong. If the user "
            "already gave the reason in the same message (\"+1500 from login bonus\"), pass it straight away. Never "
            "invent the answer yourself.",
            obj({"balance": {"type": ["integer", "string"], "description": "Current carats, e.g. 18500 or '18.5k'"},
                 "pulls": {"type": ["integer", "null"], "description": "Pulls done since the last entry (150 carats each)"},
                 "spent": {"type": ["integer", "null"], "description": "Other carats spent since the last entry"},
                 "reason": {"type": ["string", "null"], "description": "Why the balance changed, in the user's words, e.g. 'login bonus'"},
                 "category": {"type": ["string", "null"], "description": "login_bonus, missions, event, gift, shop, pulls, purchase, correction or other"},
                 "correction": {"type": ["boolean", "null"], "description": "True if the number is a correction, not income or spending"}},
                ["balance"]),
            carat_update, category=CATEGORY),
        ToolSpec("carat_status", "Show the user's current carat balance, recent entries and average daily income.",
                 obj({"days": {"type": ["integer", "null"], "description": "Window for the daily income figure (default 30)"}}),
                 carat_status, category=CATEGORY),
        ToolSpec("carat_history", "List the user's carat entries (audit log) with the reasons given for any drops.",
                 obj({"limit": {"type": ["integer", "null"]}}), carat_history, category=CATEGORY),
        ToolSpec("carat_undo", "Delete the user's last carat entry (for a mistyped balance), then they can enter it again.",
                 obj({}), carat_undo, category=CATEGORY),
    ]
