import unittest
from factorial import factorial

class TestCase(unittest.TestCase):
    """Tests for 'factorial.py'"""
    def test_zero(self):
        self.assertTrue(factorial(0) == 1)
    def test_one(self):
        self.assertTrue(factorial(1) == 1)
    def test_five(self):
        self.assertTrue(factorial(5) == 120)
    def test_ten(self):
        self.assertTrue(factorial(10) == 3628800)

if __name__ == '__main__':
    unittest.main()
