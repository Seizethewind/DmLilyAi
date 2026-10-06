"""Each user's saved veterans (finished trainees) and their simulation results, in the database.

Why a table and not Simulation/Veteran/*.json: that folder is one global folder (every user's uploads would mix)
and a host such as Render wipes its disk on each deploy. Rows are keyed by Discord/web user id, like the collection.

The store is deliberately dumb: it holds whatever veteran dict it is given. Checking a veteran (stats are numbers,
aptitude letters are S..G) is VeteranReader.normalize_veteran's job, done by the caller before save().
Merge rules match Simulation/VeteranStore.py: same name AND same five stats = the same veteran, so new skills and
missing aptitudes are merged in; same name with different stats is a different veteran.
"""
from __future__ import annotations   # the method named `list` below would otherwise shadow the builtin in annotations

import json
from typing import Any

from LilyAiCore.Helpers.clock import now_ts
from LilyAiMemory.Storage.store import MemoryStore

MAX_VETERANS = 20          # per user
MAX_RESULTS_PER_VETERAN = 20

VETERAN_SCHEMA = """
CREATE TABLE IF NOT EXISTS user_veterans (
    user_id TEXT NOT NULL,
    vet_id INTEGER NOT NULL,
    name TEXT,
    data TEXT NOT NULL,
    updated_at REAL NOT NULL,
    PRIMARY KEY (user_id, vet_id)
);

CREATE TABLE IF NOT EXISTS user_sim_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    vet_id INTEGER NOT NULL,
    course TEXT NOT NULL,
    summary TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_sim_results_vet ON user_sim_results(user_id, vet_id);
"""


class VeteranLimitError(Exception):
    """The user already has MAX_VETERANS saved."""


def _decode(row: dict[str, Any]) -> dict[str, Any]:
    return {"vet_id": int(row["vet_id"]), "name": row.get("name"), "vet": json.loads(row["data"]),
            "updated_at": row["updated_at"]}


class VeteranStore:
    def __init__(self, store: MemoryStore):
        self.db = store.db
        self.db.executescript(VETERAN_SCHEMA)

    # ------------------------------------------------------------------ veterans

    def list(self, user_id: str) -> list[dict[str, Any]]:
        rows = self.db.query("SELECT vet_id, name, data, updated_at FROM user_veterans WHERE user_id=? ORDER BY vet_id", (user_id,))
        return [_decode(r) for r in rows]

    def get(self, user_id: str, vet_id: int) -> dict[str, Any] | None:
        row = self.db.query_one(
            "SELECT vet_id, name, data, updated_at FROM user_veterans WHERE user_id=? AND vet_id=?", (user_id, int(vet_id)))
        return _decode(row) if row else None

    def find(self, user_id: str, ref: Any) -> list[dict[str, Any]]:
        """Veterans matching `ref`: a number or "#3" (the id), else a name. An exact name wins over a partial one."""
        text = str(ref).strip().lstrip("#").strip()
        rows = self.list(user_id)
        if text.isdigit():
            return [r for r in rows if r["vet_id"] == int(text)]
        low = text.lower()
        exact = [r for r in rows if (r["name"] or "").lower() == low]
        return exact or [r for r in rows if low and low in (r["name"] or "").lower()]

    def save(self, user_id: str, vet: dict[str, Any]) -> tuple[int, str]:
        """Store a (checked) veteran. Returns (vet_id, status): created | updated | unchanged.
        Raises VeteranLimitError when a new veteran would go over MAX_VETERANS."""
        rows = self.list(user_id)
        for r in rows:
            old = r["vet"]
            if old.get("name") == vet.get("name") and old.get("stats") == vet.get("stats"):
                seen = {s.lower() for s in old.get("skills", [])}
                fresh = [s for s in vet.get("skills", []) if s.lower() not in seen]
                changed = bool(fresh)
                old["skills"] = [*old.get("skills", []), *fresh]
                for cat, group in vet.get("aptitudes", {}).items():
                    for key, letter in group.items():
                        if letter is not None and old.get("aptitudes", {}).get(cat, {}).get(key) is None:
                            old.setdefault("aptitudes", {}).setdefault(cat, {})[key] = letter
                            changed = True
                if changed:
                    self.db.execute("UPDATE user_veterans SET data=?, updated_at=? WHERE user_id=? AND vet_id=?",
                                    (json.dumps(old, ensure_ascii=False), now_ts(), user_id, r["vet_id"]))
                return r["vet_id"], "updated" if changed else "unchanged"
        if len(rows) >= MAX_VETERANS:
            raise VeteranLimitError(f"You already have {MAX_VETERANS} veterans saved. Delete one first.")
        vet_id = max((r["vet_id"] for r in rows), default=0) + 1
        self.db.execute(
            "INSERT INTO user_veterans(user_id, vet_id, name, data, updated_at) VALUES (?,?,?,?,?)",
            (user_id, vet_id, vet.get("name"), json.dumps(vet, ensure_ascii=False), now_ts()))
        return vet_id, "created"

    def delete(self, user_id: str, vet_id: int) -> bool:
        existed = self.get(user_id, vet_id) is not None
        if existed:
            self.db.execute("DELETE FROM user_veterans WHERE user_id=? AND vet_id=?", (user_id, int(vet_id)))
            self.db.execute("DELETE FROM user_sim_results WHERE user_id=? AND vet_id=?", (user_id, int(vet_id)))
        return existed

    # ------------------------------------------------------------------ simulation results

    def add_result(self, user_id: str, vet_id: int, course: str, summary: str) -> None:
        self.db.execute(
            "INSERT INTO user_sim_results(user_id, vet_id, course, summary, created_at) VALUES (?,?,?,?,?)",
            (user_id, int(vet_id), str(course), summary, now_ts()))
        self.db.execute(
            "DELETE FROM user_sim_results WHERE user_id=? AND vet_id=? AND id NOT IN ("
            "SELECT id FROM user_sim_results WHERE user_id=? AND vet_id=? ORDER BY id DESC LIMIT ?)",
            (user_id, int(vet_id), user_id, int(vet_id), MAX_RESULTS_PER_VETERAN))

    def results(self, user_id: str, vet_id: int, limit: int = 5) -> list[dict[str, Any]]:
        return self.db.query(
            "SELECT course, summary, created_at FROM user_sim_results WHERE user_id=? AND vet_id=? ORDER BY id DESC LIMIT ?",
            (user_id, int(vet_id), int(limit)))

    def result_count(self, user_id: str, vet_id: int) -> int:
        return int(self.db.query_one(
            "SELECT COUNT(*) AS n FROM user_sim_results WHERE user_id=? AND vet_id=?", (user_id, int(vet_id)))["n"])

    # ------------------------------------------------------------------ whole user

    def clear(self, user_id: str) -> int:
        n = len(self.list(user_id))
        self.db.execute("DELETE FROM user_veterans WHERE user_id=?", (user_id,))
        self.db.execute("DELETE FROM user_sim_results WHERE user_id=?", (user_id,))
        return n
