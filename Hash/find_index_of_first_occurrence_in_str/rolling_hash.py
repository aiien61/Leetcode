"""
Returns the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

e.g.
haystack = "abcdede"
needle = "de"
The index of "de" = 3
"""
from typing import Optional


class RollingHashSolution:
    def __init__(self):
        self.magic_number: int = 31
        self.module_number: int = 1_000_000_007

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
        needle_hash: int = self.hashed(needle)
        haystack_hash: Optional[int] = None
        
        for i in range(n-m+1):
            if haystack_hash is None:
                haystack_hash = self.hashed(haystack[i: i+m])
            else:
                haystack_hash -= ord(haystack[i-1]) * pow(self.magic_number, m-1) % self.module_number
                haystack_hash = self.mod(haystack_hash, self.module_number)
                haystack_hash = (haystack_hash * self.magic_number) % self.module_number
                haystack_hash = (haystack_hash+ ord(haystack[i+m-1])) % self.module_number

            if haystack_hash == needle_hash and haystack[i: i+m] == needle:
                return i
        
        return -1

    def mod(self, a: int, b: int) -> int:
        return (a % b + b) % b

    def hashed(self, s: str) -> int:
        result: int = 0
        for char in s:
            result = (result * self.magic_number + ord(char)) % self.module_number
        return result

                
            



