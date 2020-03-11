"""

5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

==================================================================
at first
It's time limit exceeded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def l(s):
            if len(s) == 1 or len(s) == 0:
                return s
            if s[0] == s[-1]:
                len_half = len(s) // 2
                _s = s[len(s) - len_half:]
                if s[0:len_half] == _s[::-1]:
                    return s

            result_a = l(s[1:])
            result_b = l(s[:-1])

            if result_a and result_b:
                if len(result_a) > len(result_b):
                    return result_a
                return result_b

        return l(s)
==================================================================

My opinion:
I want to make more faster code.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                c = s[i:j]
                idx = len(c) // 2
                # palindromic
                _c = c[len(c) - idx:]
                if c[:idx] == _c[::-1]:
                    if max_len < len(c):
                        max_len = len(c)
                        result = c
        if max_len == 0:
            result = s
        return result
