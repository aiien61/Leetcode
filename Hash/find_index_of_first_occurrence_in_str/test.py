import unittest
from brutal_force import BrutalForceSolution
from rolling_hash import RollingHashSolution
from built_in_hash import BuiltInHashSolution

class TestStrFinder(unittest.TestCase):
    def setUp(self):
        self.brutal_force = BrutalForceSolution()
        self.rolling_hash = RollingHashSolution()
        self.built_in_hash = BuiltInHashSolution()

    def test_find_str_match_at_beginning(self):
        haystack: str = "sadbutsad"
        needle: str = "sad"
        
        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = 0
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = 0
        self.assertEqual(actual, expected)

        actual: int = self.built_in_hash.strStr(haystack, needle)
        expected: int = 0
        self.assertEqual(actual, expected)

    def test_fail_find_str_match(self):
        haystack: str = "leetcode"
        needle: str = "leeto"
        
        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

        actual: int = self.built_in_hash.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

    def test_find_str_match_in_middle(self):
        haystack: str = "abcdede"
        needle: str = "de"
        
        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = 3
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = 3
        self.assertEqual(actual, expected)

        actual: int = self.built_in_hash.strStr(haystack, needle)
        expected: int = 3
        self.assertEqual(actual, expected)

    def test_find_str_match_at_last(self):
        haystack: str = "abcdefg"
        needle: str = "fg"

        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = 5
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = 5
        self.assertEqual(actual, expected)

        actual: int = self.built_in_hash.strStr(haystack, needle)
        expected: int = 5
        self.assertEqual(actual, expected)

    def test_fail_find_str_match_when_null_target(self):
        haystack: str = "abcdefg"
        needle: str = ""

        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

        actual: int = self.built_in_hash.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)


    def test_fail_find_str_match_when_target_is_longer(self):
        haystack: str = "abcdefg"
        needle: str = "abcdefgh"

        actual: int = self.brutal_force.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)

        actual: int = self.rolling_hash.strStr(haystack, needle)
        expected: int = -1
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
