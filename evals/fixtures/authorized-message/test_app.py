import unittest
from app import validation_error
class MessageTest(unittest.TestCase):
    def test_current_response(self):
        self.assertIn("error", validation_error())
