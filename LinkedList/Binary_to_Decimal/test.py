import unittest
from exercise1 import SolutionList

class TestBinaryToDecimal(unittest.TestCase):
    def test_binary_to_decimal_when_binary_110(self):
        ll = SolutionList(1)
        ll.append(1)
        ll.append(0)
        expected = 6
        actual = ll.binary_to_decimal()
        self.assertEqual(expected, actual)

    def test_binary_to_decimal_when_binary_1000(self):
        ll = SolutionList(1)
        ll.append(0)
        ll.append(0)
        ll.append(0)
        expected = 8
        actual = ll.binary_to_decimal()
        self.assertEqual(expected, actual)        

    def test_binary_to_decimal_when_binary_0(self):
        ll = SolutionList(0)
        expected = 0
        actual = ll.binary_to_decimal()
        self.assertEqual(expected, actual)        

    def test_binary_to_decimal_when_binary_1(self):
        ll = SolutionList(1)
        expected = 1
        actual = ll.binary_to_decimal()
        self.assertEqual(expected, actual)

    def test_binary_to_decimal_when_binary_1101(self):
        ll = SolutionList(1)
        ll.append(1)
        ll.append(0)
        ll.append(1)
        expected = 13
        actual = ll.binary_to_decimal()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
