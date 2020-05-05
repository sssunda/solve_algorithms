"""

20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            elif stack:
                if bracket == brackets[stack[-1]]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False

        if stack:
            return False
        return True