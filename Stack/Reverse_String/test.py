import unittest
from exercise1 import reverse_string

class TestReverseString(unittest.TestCase):

    def test_reverse_string_when_parameter_is_helloworld(self):
        string: str = 'helloworld'
        expected: str = 'dlrowolleh'
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

    def test_reverse_string_when_empty_string(self):
        string: str = ''
        expected: str = ''
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

    def test_reverse_string_when_parameter_is_single_letter_k(self):
        string: str = 'k'
        expected: str = 'k'
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

    def test_reverse_string_when_parameter_is_two_characters_ab(self):
        string: str = 'ab'
        expected: str = 'ba'
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

    def test_reverse_string_when_parameter_is_palindrome_abba(self):
        string: str = 'abba'
        expected: str = 'abba'
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

    def test_reverse_string_when_parameter_is_numbers_and_special_characters(self):
        string: str = '1!2@3#4$5%6^7&8*9(0)'
        expected: str = string[::-1]
        actual: str = reverse_string(string)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
