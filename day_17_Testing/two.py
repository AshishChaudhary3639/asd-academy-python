from one import addition,subtraction
import unittest

class MyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(10,5),15)

    def test_subtraction(self):
        self.assertEqual(subtraction(8,5),2)

if __name__=='__main__':
    print(__name__)
    unittest.main()