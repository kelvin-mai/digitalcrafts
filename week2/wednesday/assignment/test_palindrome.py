import unittest
from palindrome import is_palindrome

class TestCase(unittest.TestCase):
    """Tests for 'palindrome.py'"""
    def test_racecar(self):
        self.assertTrue(is_palindrome('racecar'))
    def test_cat(self):
        self.assertFalse(is_palindrome('cat'))
    def test_cases(self):
        self.assertTrue(is_palindrome('Racecar'))
    def test_spaces(self):
        self.assertTrue(is_palindrome('race car'))

if __name__ == '__main__':
    unittest.main()
