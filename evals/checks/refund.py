from datetime import date, timedelta
import unittest
from app import eligible
class RefundContract(unittest.TestCase):
    def test_calendar_boundaries(self):
        start = date(2026, 2, 20)
        for days, expected in [(-1, False), (0, True), (30, True), (31, False)]:
            with self.subTest(days=days):
                self.assertIs(eligible(start, start + timedelta(days=days)), expected)
    def test_uncaptured(self):
        self.assertIs(eligible(None, date(2026, 1, 1)), False)
    def test_not_tied_to_today(self):
        self.assertIs(eligible(date(2020, 12, 31), date(2021, 1, 30)), True)
if __name__ == '__main__':
    unittest.main(verbosity=2)
