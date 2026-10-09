"""Turso (libSQL) database adapter.

Same call surface as ExternalServices.Database.sqlite.Database
(execute/executescript/query/query_one/close), so this is a drop-in swap
for any domain that only depends on the Database interface — nothing in
LilyAiMemory or elsewhere needs to change to use it.

Uses an embedded replica: a local libSQL file that syncs against the
remote Turso primary. Reads hit the local file (fast, works even if the
network is briefly down); writes go through and replicate on the next
sync() call.

Stale remote streams: writes (and sync) travel to the Turso primary over a
Hrana stream that the server drops after it has been idle for a while. The next
call on that connection then fails with e.g. "Hrana: api error: status=404 Not
Found ... stream not found". Every operation here therefore retries exactly once on
a fresh connection when it sees that error, instead of letting it escape - before this,
an idle spell (such as the Discord reconnect cooldown) turned the next DB write into an
unhandled ValueError.
"""
import threading
from pathlib import Path
from typing import Any, Callable, Iterable, TypeVar

import libsql_experimental as libsql

from LilyAiCore.Logging.logger import get_logger

log = get_logger("database.turso")

T = TypeVar("T")


def _is_stale_stream_error(exc: BaseException) -> bool:
    """True for the errors Turso returns when the server has dropped our idle stream."""
    msg = str(exc).lower()
    return "stream not found" in msg or "stream expired" in msg or ("hrana" in msg and "404" in msg)


class TursoDatabase:
    def __init__(
        self,
        path: str | Path,
        sync_url: str,
        auth_token: str,
        sync_interval_s: float | None = 60.0,
    ):
        self._path = str(path)
        self._sync_url = sync_url
        self._auth_token = auth_token
        # The installed libsql_experimental build has no built-in periodic sync
        # (no sync_period kwarg on connect()), so background sync is driven here
        # with a plain threading.Timer instead.
        self._conn = self._connect()
        self._lock = threading.Lock()
        self._sync_interval_s = sync_interval_s
        self._timer: threading.Timer | None = None
        self.sync()
        if sync_interval_s:
            self._schedule_sync()

    def _connect(self):
        return libsql.connect(self._path, sync_url=self._sync_url, auth_token=self._auth_token)

    def _reconnect(self) -> None:
        """Replace the connection with a fresh one. Caller must hold self._lock."""
        try:
            self._conn.close()
        except Exception:  # the old stream is already dead; nothing to clean up
            pass
        self._conn = self._connect()
        try:
            self._conn.sync()
        except Exception as e:
            log.warning("sync after Turso reconnect failed: %s", e)

    def _run(self, fn: Callable[[], T]) -> T:
        """Run fn; if Turso reports a stale stream, reconnect and run it once more.
        Caller must hold self._lock. Any other error, or a second stale-stream error,
        propagates unchanged."""
        try:
            return fn()
        except Exception as e:
            if not _is_stale_stream_error(e):
                raise
            log.warning("Turso stream went stale (%s); reconnecting and retrying once", e)
            self._reconnect()
            return fn()

    def _schedule_sync(self) -> None:
        self._timer = threading.Timer(self._sync_interval_s, self._sync_and_reschedule)
        self._timer.daemon = True
        self._timer.start()

    def _sync_and_reschedule(self) -> None:
        try:
            self.sync()
        except Exception as e:
            log.warning("background Turso sync failed: %s", e)
        finally:
            if self._sync_interval_s:
                self._schedule_sync()

    def sync(self) -> None:
        with self._lock:
            self._run(lambda: self._conn.sync())

    def execute(self, sql: str, params: Iterable[Any] = ()) -> int:
        params = tuple(params)

        def op() -> int:
            cur = self._conn.execute(sql, params)
            self._conn.commit()
            return cur.lastrowid or 0

        with self._lock:
            return self._run(op)

    def executescript(self, script: str) -> None:
        # libsql_experimental doesn't expose sqlite3's executescript, so run each
        # statement individually. Schemas here are plain CREATE TABLE/INDEX
        # statements with no string literals containing ';', so a naive split is safe.
        # They are also idempotent (IF NOT EXISTS), which keeps the one retry after a
        # reconnect safe even if the first attempt got partway through.
        statements = [s for s in (s.strip() for s in script.split(";")) if s]

        def op() -> None:
            for statement in statements:
                self._conn.execute(statement)
            self._conn.commit()

        with self._lock:
            self._run(op)

    def query(self, sql: str, params: Iterable[Any] = ()) -> list[dict[str, Any]]:
        params = tuple(params)

        def op() -> list[dict[str, Any]]:
            cur = self._conn.execute(sql, params)
            cols = [d[0] for d in cur.description]
            return [dict(zip(cols, row)) for row in cur.fetchall()]

        with self._lock:
            return self._run(op)

    def query_one(self, sql: str, params: Iterable[Any] = ()) -> dict[str, Any] | None:
        rows = self.query(sql, params)
        return rows[0] if rows else None

    def close(self) -> None:
        if self._timer:
            self._timer.cancel()
        with self._lock:
            self._conn.close()
