# https://leetcode.com/problems/generate-parentheses/

from typing import List

# Our conditions are:
# * Add open bracket if open < n
# * Add closing braket if closed < open
# * Validate that closed == open == n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(Nopen, Nclosed, stack):
            if Nopen == Nclosed == n:
                tmp_result = ''.join(stack)
                result.append(tmp_result)
                return
            if Nopen < n:
                backtrack(Nopen + 1, Nclosed, stack + ['('])
            if Nclosed < Nopen:
                backtrack(Nopen, Nclosed + 1, stack + [')'])
        
        backtrack(0, 0, [])
        return result