# test_calculator.py

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(1, 1), 3)
        self.assertIsInstance(add(10, 5), int)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertGreater(subtract(10, 2), 5)
        self.assertLess(subtract(5, 10), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertTrue(multiply(0, 5) == 0)
        self.assertIsNotNone(multiply(3, 3))

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(5, 3), 1.6667, places=4)
        self.assertIsNone(divide(10, 0))  # Division by zero returns None
        self.assertIsNotNone(divide(10, 2))
        self.assertIsInstance(divide(8, 4), float)

if __name__ == '__main__':
    unittest.main()
