import unittest
from app import validation_error
class MessageContract(unittest.TestCase):
    def test_exact_response(self):
        self.assertEqual(validation_error(), {"error": "Currency is invalid"})
    def test_stable_result(self):
        self.assertEqual(validation_error(), validation_error())
if __name__ == "__main__":
    unittest.main(verbosity=2)
