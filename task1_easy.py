"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        counter = {}

        for i in s:
            counter[i] = counter.setdefault(i, 0) + 1

        for i in t:
            if i not in counter or counter[i] == 0:
                return False
            counter[i] -= 1

        return True