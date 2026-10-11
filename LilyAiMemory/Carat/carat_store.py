"""Each user's carat balance log: one row per time they told the bot their balance.

The balance the user types is the source of truth. Income is derived: new balance - old balance (+ whatever was
spent in between, when the user says so). A drop is never counted as income; the caller must say why it dropped,
and that reason is stored with the row (the audit trail).
"""
from __future__ import annotations

from typing import Any

from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Storage.store import MemoryStore

CARATS_PER_PULL = 150
MAX_ROWS = 1000   # per user; the oldest are trimmed

CARAT_SCHEMA = """
CREATE TABLE IF NOT EXISTS user_carat_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    ts REAL NOT NULL,
    balance INTEGER NOT NULL,
    income INTEGER NOT NULL DEFAULT 0,
    spent INTEGER NOT NULL DEFAULT 0,
    kind TEXT NOT NULL,
    note TEXT
);
CREATE INDEX IF NOT EXISTS idx_carat_log_user ON user_carat_log(user_id, id);
"""


class CaratError(ValueError):
    """The entry cannot be recorded as given; the message says what to ask the user."""


def classify(prev: int | None, balance: int, spent: int | None = None, correction: bool = False) -> dict[str, Any]:
    """Work out one entry. Returns {kind, income, spent, delta} or raises CaratError.

    kind: baseline (first entry or a correction), gain, same, spend (balance fell and the user said why).
    Income is never negative: a fall must be explained by `spent` (pulls, purchases) or marked as a correction.
    """
    if balance < 0:
        raise CaratError("A carat balance cannot be negative.")
    if prev is None:
        return {"kind": "baseline", "income": 0, "spent": 0, "delta": 0}
    delta = balance - prev
    if correction:
        return {"kind": "baseline", "income": 0, "spent": 0, "delta": delta}
    if spent is None:
        if delta < 0:
            raise CaratError(
                f"The balance fell by {-delta:,} (from {prev:,} to {balance:,}). Do not record it yet: ask the user what "
                f"happened. Pulls ({-delta / CARATS_PER_PULL:g} pulls at {CARATS_PER_PULL} each if that is all it was), "
                "something else they spent carats on, or a typo/wrong number to correct.")
        return {"kind": "gain" if delta > 0 else "same", "income": delta, "spent": 0, "delta": delta}
    if spent < 0:
        raise CaratError("Spent carats cannot be negative.")
    income = delta + spent
    if income < 0:
        raise CaratError(
            f"Spending {spent:,} does not explain the drop: the balance fell by {-delta:,}, which is {-income:,} more "
            "than that. Ask the user what else happened (more pulls, a purchase, a wrong number).")
    return {"kind": "spend", "income": income, "spent": spent, "delta": delta}


class CaratStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db
        self.db.executescript(CARAT_SCHEMA)

    def last(self, user_id: str) -> dict[str, Any] | None:
        return self.db.query_one(
            "SELECT id, ts, balance, income, spent, kind, note FROM user_carat_log WHERE user_id=? ORDER BY id DESC LIMIT 1",
            (user_id,))

    def recent(self, user_id: str, limit: int = 10) -> list[dict[str, Any]]:
        return self.db.query(
            "SELECT id, ts, balance, income, spent, kind, note FROM user_carat_log WHERE user_id=? ORDER BY id DESC LIMIT ?",
            (user_id, int(limit)))

    def add(self, user_id: str, balance: int, income: int, spent: int, kind: str, note: str | None, ts: float | None = None) -> int:
        self.db.execute(
            "INSERT INTO user_carat_log(user_id, ts, balance, income, spent, kind, note) VALUES (?,?,?,?,?,?,?)",
            (user_id, ts if ts is not None else now_ts(), int(balance), int(income), int(spent), kind, note))
        self.db.execute(
            "DELETE FROM user_carat_log WHERE user_id=? AND id NOT IN ("
            "SELECT id FROM user_carat_log WHERE user_id=? ORDER BY id DESC LIMIT ?)", (user_id, user_id, MAX_ROWS))
        return int(self.last(user_id)["id"])

    def delete_last(self, user_id: str) -> dict[str, Any] | None:
        row = self.last(user_id)
        if row:
            self.db.execute("DELETE FROM user_carat_log WHERE user_id=? AND id=?", (user_id, row["id"]))
        return row

    def totals(self, user_id: str, since_ts: float | None = None) -> dict[str, Any]:
        """Income and spending since `since_ts` (or ever). The first row of a window is its baseline, so its own
        income is not counted when the window starts at a row; the caller passes the ts of the baseline row."""
        q = "SELECT COALESCE(SUM(income),0) AS income, COALESCE(SUM(spent),0) AS spent, COUNT(*) AS n FROM user_carat_log WHERE user_id=?"
        args: list[Any] = [user_id]
        if since_ts is not None:
            q += " AND ts>?"
            args.append(since_ts)
        return self.db.query_one(q, tuple(args))

    def window(self, user_id: str, days: float, now: float | None = None) -> dict[str, Any] | None:
        """Income rate over the last `days`: from the newest row at or before the window start (or the first row)
        to the latest row. None if there are fewer than two rows."""
        now = now if now is not None else now_ts()
        last = self.last(user_id)
        if not last:
            return None
        start = self.db.query_one(
            "SELECT id, ts FROM user_carat_log WHERE user_id=? AND ts<=? ORDER BY id DESC LIMIT 1", (user_id, now - days * 86400))
        if not start:
            start = self.db.query_one("SELECT id, ts FROM user_carat_log WHERE user_id=? ORDER BY id ASC LIMIT 1", (user_id,))
        if not start or start["id"] == last["id"]:
            return None
        t = self.db.query_one(
            "SELECT COALESCE(SUM(income),0) AS income, COALESCE(SUM(spent),0) AS spent FROM user_carat_log WHERE user_id=? AND id>?",
            (user_id, start["id"]))
        span = max((last["ts"] - start["ts"]) / 86400, 1e-9)
        return {"days": span, "income": int(t["income"]), "spent": int(t["spent"]), "per_day": t["income"] / span}

    def clear(self, user_id: str) -> int:
        n = int(self.db.query_one("SELECT COUNT(*) AS n FROM user_carat_log WHERE user_id=?", (user_id,))["n"])
        self.db.execute("DELETE FROM user_carat_log WHERE user_id=?", (user_id,))
        return n
