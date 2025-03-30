"""
Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

e.g.
haystack = "abcdede"
needle = "de"
The index of "de" = 3
"""


class BuiltInHashSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack or not needle:
            return -1
        elif len(haystack) < len(needle):
            return -1

        n, m = len(haystack), len(needle)
        needle_hash: int = hash(needle)

        for i in range(n - m + 1):
            if hash(haystack[i: i+m]) == needle_hash:
                return i
        return -1
