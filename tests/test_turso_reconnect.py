"""Regression tests for the stale-Turso-stream crash.

Production symptom: after the Discord reconnect cooldown (~40 min idle), the next database write
failed with ValueError('Hrana: `api error: `status=404 Not Found, body={"error":"stream not found: ..."}``'),
which escaped LilyDiscordClient.run_forever(), ended the discord task, made main.py exit, and
had Render restart the container (another Discord login from a Cloudflare-blocked IP).

Run:  python -m unittest discover -s tests -v
"""
import sys
import types
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
# The real driver isn't needed (and may not be installed): turso.libsql is patched per test.
sys.modules.setdefault("libsql_experimental", types.ModuleType("libsql_experimental"))

from LilyAiCore.ExternalServices.Database import turso  # noqa: E402
from LilyAiCore.ExternalServices.Discord.reconnect_state import ReconnectState  # noqa: E402

STALE = ValueError('Hrana: `api error: `status=404 Not Found, body={"error":"stream not found: 032871f4:492d4f8"}``')


class FakeCursor:
    def __init__(self, rows=(), cols=("id", "name")):
        self.description = [(c,) for c in cols]
        self._rows = list(rows)
        self.lastrowid = 7

    def fetchall(self):
        return self._rows


class FakeConn:
    def __init__(self, rows, fail_with=None, always=False):
        self.rows, self.fail_with, self.always = rows, fail_with, always
        self.executed, self.commits, self.syncs, self.closed = [], 0, 0, False

    def _maybe_fail(self):
        if self.fail_with is not None:
            err = self.fail_with
            if not self.always:
                self.fail_with = None
            raise err

    def execute(self, sql, params=()):
        self._maybe_fail()
        self.executed.append((sql, params))
        return FakeCursor(self.rows)

    def commit(self):
        self.commits += 1

    def sync(self):
        self._maybe_fail()
        self.syncs += 1

    def close(self):
        self.closed = True


class FakeLibsql:
    """connect() hands out the queued connections in order."""

    def __init__(self, *conns):
        self.conns = list(conns)
        self.connects = 0

    def connect(self, path, sync_url=None, auth_token=None):
        self.connects += 1
        return self.conns.pop(0)


def _db(*conns):
    lib = FakeLibsql(*conns)
    patcher = mock.patch.object(turso, "libsql", lib)
    patcher.start()
    db = turso.TursoDatabase("/tmp/x.db", "libsql://x", "tok", sync_interval_s=None)
    return db, lib, patcher


class StaleStreamTests(unittest.TestCase):
    def tearDown(self):
        mock.patch.stopall()

    def test_execute_reconnects_and_retries_once(self):
        stale, fresh = FakeConn([]), FakeConn([])
        db, lib, _ = _db(stale, fresh)
        stale.fail_with = STALE                      # goes stale after construction (idle)
        self.assertEqual(db.execute("INSERT INTO t VALUES (1)"), 7)
        self.assertEqual(lib.connects, 2)
        self.assertTrue(stale.closed)
        self.assertEqual(fresh.executed, [("INSERT INTO t VALUES (1)", ())])
        self.assertEqual(fresh.commits, 1)

    def test_query_reconnects_and_retries_once(self):
        stale, fresh = FakeConn([]), FakeConn([(1, "a")])
        db, lib, _ = _db(stale, fresh)
        stale.fail_with = STALE
        self.assertEqual(db.query("SELECT * FROM t"), [{"id": 1, "name": "a"}])
        self.assertEqual(lib.connects, 2)

    def test_executescript_reconnects_and_retries_once(self):
        stale, fresh = FakeConn([]), FakeConn([])
        db, lib, _ = _db(stale, fresh)
        stale.fail_with = STALE
        db.executescript("CREATE TABLE IF NOT EXISTS a (x); CREATE TABLE IF NOT EXISTS b (y);")
        self.assertEqual(len(fresh.executed), 2)
        self.assertEqual(fresh.commits, 1)

    def test_sync_reconnects_and_retries_once(self):
        stale, fresh = FakeConn([]), FakeConn([])
        db, lib, _ = _db(stale, fresh)
        stale.fail_with = STALE
        db.sync()
        self.assertEqual(lib.connects, 2)

    def test_other_errors_do_not_reconnect(self):
        conn = FakeConn([])
        db, lib, _ = _db(conn)
        conn.fail_with = ValueError("near 'SELEC': syntax error")
        with self.assertRaises(ValueError):
            db.execute("SELEC 1")
        self.assertEqual(lib.connects, 1)

    def test_stale_twice_gives_up_instead_of_looping(self):
        stale, also_stale = FakeConn([]), FakeConn([], fail_with=STALE, always=True)
        db, lib, _ = _db(stale, also_stale)
        stale.fail_with = STALE
        with self.assertRaises(ValueError):
            db.execute("INSERT INTO t VALUES (1)")
        self.assertEqual(lib.connects, 2)

    def test_background_sync_failure_is_logged_not_raised(self):
        conn = FakeConn([])
        db, lib, _ = _db(conn)
        db._sync_interval_s = None
        conn.fail_with, conn.always = ValueError("network down"), True
        db._sync_and_reschedule()  # must not raise


class BrokenDb:
    def executescript(self, script):
        pass

    def query_one(self, *a, **k):
        raise STALE

    def execute(self, *a, **k):
        raise STALE


class ReconnectStateTests(unittest.TestCase):
    def test_db_errors_never_escape(self):
        state = ReconnectState(BrokenDb())
        self.assertEqual(state.get(), (0.0, 0.0))   # starts fresh
        state.set(123.0, 2400.0)                      # must not raise
        state.clear()                                 # must not raise

    def test_still_persists_when_db_is_healthy(self):
        import sqlite3

        class Mem:
            def __init__(self):
                self.c = sqlite3.connect(":memory:")
                self.c.row_factory = sqlite3.Row

            def executescript(self, s):
                self.c.executescript(s)

            def execute(self, sql, params=()):
                self.c.execute(sql, tuple(params))
                self.c.commit()

            def query_one(self, sql, params=()):
                r = self.c.execute(sql, tuple(params)).fetchone()
                return dict(r) if r else None

        state = ReconnectState(Mem())
        self.assertEqual(state.get(), (0.0, 0.0))
        state.set(100.0, 600.0)
        state.set(200.0, 1200.0)
        self.assertEqual(state.get(), (200.0, 1200.0))
        state.clear()
        self.assertEqual(state.get(), (0.0, 0.0))


if __name__ == "__main__":
    unittest.main()
