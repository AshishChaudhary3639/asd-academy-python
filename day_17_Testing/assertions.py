import unittest

class TestAssertions(unittest.TestCase):

    def test_assertEqual_and_NotEqual(self):
        self.assertEqual(2 + 3, 5)
        self.assertNotEqual(2 * 2, 5)

    def test_assertTrue_and_False(self):
        self.assertTrue(10 > 5)
        self.assertFalse(3 > 7)

    def test_assertIs_and_IsNot(self):
        a = b = [1, 2, 3]
        c = [1, 2, 3]
        self.assertIs(a, b)        # same object
        self.assertIsNot(a, c)     # different object, even if values are same

    def test_assertIsNone_and_IsNotNone(self):
        x = None
        y = "hello"
        self.assertIsNone(x)
        self.assertIsNotNone(y)

    def test_assertIn_and_NotIn(self):
        fruits = ['apple', 'banana', 'cherry']
        self.assertIn('banana', fruits)
        self.assertNotIn('grape', fruits)

    def test_assertIsInstance_and_NotIsInstance(self):
        self.assertIsInstance(10,int)
        self.assertNotIsInstance(10, str)

    def test_assertGreater_and_Less(self):
        self.assertGreater(5, 2)
        self.assertLess(2, 5)

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(3.14159, 3.1416, places=4)

if __name__ == '__main__':
    unittest.main()
