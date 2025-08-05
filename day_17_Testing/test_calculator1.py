# test_calculator.py

import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 2), 1.5)
        self.assertEqual(divide(5, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()

# import unittest
# from calculator import add
# from calculator import subtract


# class TestDemo(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(5,4),9)
    
# if __name__=='__main__':
#     unittest.main()