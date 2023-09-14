# https://leetcode.com/problems/generate-parentheses/

from typing import List

# Our conditions are:
# * Add open bracket if open < n
# * Add closing braket if closed < open
# * Validate that closed == open == n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(n_open, n_closed, string):
            if n_open == n_closed == n:
                result.append(string)
                return
            if n_open < n:
                generate(n_open + 1, n_closed, string + '(')
            if n_closed < n_open:
                generate(n_open, n_closed + 1, string + ')')

        generate(0, 0, "")
        return result
