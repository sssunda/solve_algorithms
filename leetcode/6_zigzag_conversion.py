"""

6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 1
        idx = 0
        result = [''] * numRows

        if numRows == 1:
            return s

        for element in s:
            result[idx] += element
            if idx == 0:
                i = 1
            if idx == numRows - 1:
                i = -1
            idx += i

        return ''.join(result)
