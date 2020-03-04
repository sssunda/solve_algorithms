"""

3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        count = 0
        for i in s:
            if result.count(i) != 0:
                if count < len(result):
                    count = len(result)
                idx = result.index(i)
                result = result[idx + 1:] + i
            else:
                result += i
        if count < len(result):
            count = len(result)
        return count
