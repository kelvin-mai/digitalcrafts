import unittest
import calculator

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertTrue(calculator.add(1,2) == 3)
    def test_subtract(self):
        self.assertTrue(calculator.subtract(1,2) == -1)
    def test_multiply(self):
        self.assertTrue(calculator.multiply(1,2) == 2)
    def test_divide(self):
        self.assertTrue(calculator.divide(4,2) == 2)

if __name__ == "__main__":
    unittest.main()
