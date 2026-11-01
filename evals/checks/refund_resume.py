from datetime import date, timedelta
import unittest
from app import eligible
class ResumedContract(unittest.TestCase):
    def test_corrected_boundary(self):
        capture = date(2026, 11, 20)
        for days, expected in [(-1, False), (0, True), (14, True), (15, True), (45, True), (46, False)]:
            with self.subTest(days=days):
                self.assertIs(eligible(capture, capture + timedelta(days=days)), expected)
    def test_uncaptured(self):
        self.assertIs(eligible(None, date(2026, 1, 1)), False)
    def test_historical_dates_not_wall_clock(self):
        self.assertIs(eligible(date(2020, 12, 1), date(2021, 1, 15)), True)
if __name__ == '__main__':
    unittest.main(verbosity=2)
