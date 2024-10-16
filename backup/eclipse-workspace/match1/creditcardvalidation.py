import unittest
from cc import *

class Credit(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test_ValidateCard_valid(self):
        result = ValidateCard(date(2025,2,2))
        self.assertEqual('Valid', result)
    def test_ValidateCard_expired(self):
        with self.assertRaises(RuntimeError):
            ValidateCard(date(2025,2,2))
    def tearDown(self):
        print("teardown")

if __name__ == '__main__':
    unittest.main()