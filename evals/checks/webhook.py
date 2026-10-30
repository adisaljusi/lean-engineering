"""Held-out behavior checks. Copied into the artifact only after generation."""
import concurrent.futures
import sqlite3
import tempfile
import unittest
from pathlib import Path

from app import connect, handle_event


class WebhookContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "events.db"
        self.conn = connect(self.path)
        self.addCleanup(self.conn.close)

    def rows(self, table):
        return self.conn.execute(f"SELECT event_id, amount FROM {table} ORDER BY event_id").fetchall()

    def test_retry_has_one_effect(self):
        event = {"id": "same", "amount": 100}
        for _ in range(3):
            self.assertEqual(handle_event(self.conn, event), 200)
        self.assertEqual(self.rows("events"), [("same", 100)])
        self.assertEqual(self.rows("ledger"), [("same", 100)])

    def test_distinct_events_remain_distinct(self):
        for event_id in ("a", "b"):
            self.assertEqual(handle_event(self.conn, {"id": event_id, "amount": 25}), 200)
        self.assertEqual(self.rows("ledger"), [("a", 25), ("b", 25)])

    def test_conflicting_retry_preserves_original(self):
        handle_event(self.conn, {"id": "same", "amount": 100})
        self.assertEqual(handle_event(self.conn, {"id": "same", "amount": 101}), 409)
        self.assertEqual(self.rows("events"), [("same", 100)])
        self.assertEqual(self.rows("ledger"), [("same", 100)])

    def test_database_enforces_uniqueness(self):
        handle_event(self.conn, {"id": "same", "amount": 100})
        with self.assertRaises(sqlite3.IntegrityError):
            with self.conn:
                self.conn.execute("INSERT INTO events(event_id, amount) VALUES ('same', 100)")

    def test_failure_rolls_back_and_allows_retry(self):
        self.conn.execute("""CREATE TRIGGER reject_effect BEFORE INSERT ON ledger
                           BEGIN SELECT RAISE(ABORT, 'test database failure'); END""")
        with self.assertRaises(sqlite3.DatabaseError):
            handle_event(self.conn, {"id": "recover", "amount": 50})
        self.assertEqual(self.rows("events"), [])
        self.assertEqual(self.rows("ledger"), [])
        self.conn.execute("DROP TRIGGER reject_effect")
        self.assertEqual(handle_event(self.conn, {"id": "recover", "amount": 50}), 200)
        self.assertEqual(self.rows("ledger"), [("recover", 50)])

    def test_independent_concurrent_connections(self):
        def deliver(_):
            conn = connect(self.path)
            try:
                return handle_event(conn, {"id": "race", "amount": 7})
            finally:
                conn.close()
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            self.assertEqual(list(pool.map(deliver, range(8))), [200] * 8)
        self.assertEqual(self.rows("events"), [("race", 7)])
        self.assertEqual(self.rows("ledger"), [("race", 7)])

    def test_upgrade_preserves_valid_history(self):
        legacy = Path(self.tmp.name) / "legacy.db"
        conn = sqlite3.connect(legacy)
        conn.executescript("""
            CREATE TABLE events (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
            CREATE TABLE ledger (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
            INSERT INTO events VALUES ('old', 42), ('old', 42);
            INSERT INTO ledger VALUES ('old', 42), ('old', 42);
        """)
        conn.close()
        upgraded = connect(legacy)
        self.addCleanup(upgraded.close)
        self.assertEqual(handle_event(upgraded, {"id": "old", "amount": 42}), 200)
        for table in ("events", "ledger"):
            self.assertEqual(upgraded.execute(f"SELECT event_id, amount FROM {table}").fetchall(), [("old", 42)])

    def test_upgrade_does_not_choose_conflicting_history(self):
        legacy = Path(self.tmp.name) / "conflict.db"
        conn = sqlite3.connect(legacy)
        conn.executescript("""
            CREATE TABLE events (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
            CREATE TABLE ledger (event_id TEXT NOT NULL, amount INTEGER NOT NULL);
            INSERT INTO events VALUES ('old', 42), ('old', 43);
            INSERT INTO ledger VALUES ('old', 42), ('old', 43);
        """)
        conn.close()
        try:
            upgraded = connect(legacy)
        except Exception:
            pass  # Explicitly refusing ambiguous migration is acceptable.
        else:
            upgraded.close()
            self.fail("Conflicting legacy history must require explicit resolution")
        conn = sqlite3.connect(legacy)
        self.addCleanup(conn.close)
        for table in ("events", "ledger"):
            self.assertEqual(conn.execute(f"SELECT event_id, amount FROM {table} ORDER BY amount").fetchall(),
                             [("old", 42), ("old", 43)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
