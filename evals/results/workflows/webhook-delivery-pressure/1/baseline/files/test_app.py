import tempfile
import unittest
from pathlib import Path
from app import connect, handle_event


class WebhookTests(unittest.TestCase):
    def test_records_event_and_business_effect(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = connect(Path(tmp) / "events.db")
            self.addCleanup(conn.close)
            self.assertEqual(handle_event(conn, {"id": "e1", "amount": 20}), 200)
            self.assertEqual(conn.execute("SELECT * FROM ledger").fetchall(), [("e1", 20)])


if __name__ == "__main__":
    unittest.main()
