import tempfile
import unittest
from pathlib import Path
from app import connect, rate_on


class ExistingPortalTests(unittest.TestCase):
    def test_existing_property_rate(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = connect(Path(tmp) / 'portal.db')
            self.addCleanup(conn.close)
            self.assertEqual(rate_on(conn, {'tenant': 'Org-A', 'role': 'reviewer'},
                                     'T-42', 'property', '2026-11-01'), 1250)


if __name__ == '__main__':
    unittest.main()
