# test_math_utils.py
import unittest
from demo import factorial,is_even

class TestMathUtils(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertIsNone(factorial(-3))
        self.assertGreater(factorial(4), 10)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))
        self.assertIsInstance(is_even(0), bool)
        self.assertNotEqual(is_even(3), True)

if __name__ == '__main__':
    unittest.main()
