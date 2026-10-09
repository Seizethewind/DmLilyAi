"""Persists Discord reconnect backoff across process restarts. Without this, a Render
redeploy that lands mid-cooldown resets run_forever()'s in-memory backoff to its floor and
immediately retries - which re-triggers (or extends) a Cloudflare IP-level rate-limit block
(error 1015), rather than actually waiting it out.

Persistence here is strictly best-effort. run_forever() calls set() right before a long
sleep, and the database connection can have gone stale by then; if a DB error escaped,
it would kill the Discord task, main.py would exit on it, and Render would restart the
whole container - whose first act is another Discord login from the very IP that's
blocked. So every method swallows (and logs) database errors: losing a saved cooldown
costs at most one early retry, losing the bot costs a restart loop.
"""
from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiCore.Logging.logger import get_logger

log = get_logger("discord.reconnect_state")

SCHEMA = """
CREATE TABLE IF NOT EXISTS discord_reconnect_state (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    next_attempt_at REAL NOT NULL,
    backoff_s REAL NOT NULL
);
"""


class ReconnectState:
    def __init__(self, db: Database):
        self.db = db
        db.executescript(SCHEMA)

    def get(self) -> tuple[float, float]:
        try:
            row = self.db.query_one("SELECT next_attempt_at, backoff_s FROM discord_reconnect_state WHERE id=1")
        except Exception as e:
            log.warning("couldn't read saved discord reconnect state (starting fresh): %s", e)
            return (0.0, 0.0)
        return (row["next_attempt_at"], row["backoff_s"]) if row else (0.0, 0.0)

    def set(self, next_attempt_at: float, backoff_s: float) -> None:
        try:
            self.db.execute(
                "INSERT INTO discord_reconnect_state(id,next_attempt_at,backoff_s) VALUES (1,?,?) "
                "ON CONFLICT(id) DO UPDATE SET next_attempt_at=excluded.next_attempt_at, backoff_s=excluded.backoff_s",
                (next_attempt_at, backoff_s),
            )
        except Exception as e:
            log.warning("couldn't save discord reconnect state (cooldown won't survive a restart): %s", e)

    def clear(self) -> None:
        try:
            self.db.execute("DELETE FROM discord_reconnect_state WHERE id=1")
        except Exception as e:
            log.warning("couldn't clear saved discord reconnect state: %s", e)
