from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest

from publication import Rate, StaleReview, initialize, publish


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "example.db"
        self.conn = sqlite3.connect(self.path)
        self.addCleanup(self.conn.close)
        initialize(self.conn)
        with self.conn:
            self.conn.execute("INSERT INTO sections VALUES ('A','property',1250,0)")

    def send(self, conn=None, **changes):
        args = dict(tenant="A", section="property", actor_id="u1", role="approver",
                    request_id="decision-1", expected_revision=0,
                    rate=Rate(1300), reason="Reviewed signed evidence")
        args.update(changes)
        return publish(conn or self.conn, **args)

    def state(self):
        return self.conn.execute("SELECT bps,revision FROM sections").fetchone()

    def test_precise_rate_boundaries(self):
        for value in (None, True, 1.5, -1, 10001):
            with self.subTest(value=value), self.assertRaises(ValueError):
                Rate(value)
        self.assertEqual(Rate(0).bps, 0)
        self.assertEqual(Rate(10000).bps, 10000)

    def test_database_rejects_invalid_shared_write(self):
        with self.assertRaises(sqlite3.IntegrityError):
            with self.conn:
                self.conn.execute("UPDATE sections SET bps=1.5")
        self.assertEqual(self.state(), (1250, 0))

    def test_retry_and_identity_conflict(self):
        self.assertEqual(self.send(), 1)
        self.assertEqual(self.send(), 1)
        with self.assertRaises(ValueError):
            self.send(rate=Rate(1400))
        self.assertEqual(self.state(), (1300, 1))
        self.assertEqual(self.conn.execute("SELECT count(*) FROM decisions").fetchone()[0], 1)

    def test_other_connection_stale_review_cannot_overwrite(self):
        with closing(sqlite3.connect(self.path)) as other:
            self.send()
            with self.assertRaises(StaleReview):
                self.send(other, request_id="decision-2", rate=Rate(1400))
        self.assertEqual(self.state(), (1300, 1))

    def test_failure_after_update_rolls_back_both_effects(self):
        self.conn.execute("""CREATE TRIGGER deny_decision BEFORE INSERT ON decisions
            BEGIN SELECT RAISE(ABORT, 'simulated storage failure'); END""")
        with self.assertRaises(sqlite3.IntegrityError):
            self.send()
        self.assertEqual(self.state(), (1250, 0))
        self.assertEqual(self.conn.execute("SELECT count(*) FROM decisions").fetchone()[0], 0)
        self.conn.execute("DROP TRIGGER deny_decision")
        self.assertEqual(self.send(), 1)

    def test_permissions_and_tenant_scope(self):
        with self.assertRaises(PermissionError):
            self.send(role="reviewer")
        with self.assertRaises(StaleReview):
            self.send(tenant="B")
        self.assertEqual(self.state(), (1250, 0))


if __name__ == "__main__":
    unittest.main()
