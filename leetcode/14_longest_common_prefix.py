"""

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        word = min(strs, key=len)
        strs.remove(word)
        idx = 0
        result = ""
        while idx < len(word):
            flag = True
            for element in strs:
                if element[idx] != word[idx]:
                    flag = False
                    break
            if flag:
                result += word[idx]
                idx += 1
            else:
                break

        return result
