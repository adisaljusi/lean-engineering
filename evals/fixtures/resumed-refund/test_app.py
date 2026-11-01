from datetime import date
import unittest
from app import eligible
class RefundSmoke(unittest.TestCase):
    def test_uncaptured(self):
        self.assertFalse(eligible(None, date(2026, 1, 1)))
