import unittest
from exercise1 import is_balanced_parentheses

class Test(unittest.TestCase):
    def test_is_balanced_parentheses_when_balanced_nested_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('((()))')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_single_paired_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('()')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_two_paired_balanced_in_nested_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('(()())')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_imbalanced_extra_left_parenthese(self):
        expected: bool = False
        actual: bool = is_balanced_parentheses('(()')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_imbalanced_extra_right_parenthese(self):
        expected: bool = False
        actual: bool = is_balanced_parentheses('())')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_close_parenthese_followed_by_open_parenthese(self):
        expected: bool = False
        actual: bool = is_balanced_parentheses(')(')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_empty_string(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_multiple_paired_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('()()()()')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_two_paired_nested_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('(())(())')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_three_paired_parentheses_in_nested_parentheses(self):
        expected: bool = True
        actual: bool = is_balanced_parentheses('(()()())')
        self.assertEqual(expected, actual)

    def test_is_balanced_parentheses_when_imbalanced_nested_parentheses(self):
        expected: bool = False
        actual: bool = is_balanced_parentheses('((())')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
