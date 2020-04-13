"""

17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

My opinion:
It failed. I searched about DFS.

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                       '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return digits_dict[digits]

        digits_list = []
        for digit in digits:
            digits_list.append(digits_dict[digit])

        stack = [("", 0)]
        result = []

        while stack:
            temp_str, idx = stack.pop()
            if len(temp_str) == len(digits):
                result.append(temp_str)

            if idx < len(digits):
                for digit in digits_list[idx]:
                    stack.append((temp_str + digit, idx + 1))
        return result