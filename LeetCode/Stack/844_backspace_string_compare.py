# https://leetcode.com/problems/backspace-string-compare/

# O(n) memory complexity
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def make_stack(s: str):
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack

        return make_stack(s) == make_stack(t)

# Optional - O(1) memory complexity
# https://leetcode.com/problems/backspace-string-compare/solutions/3053688/python-simple-solution-beats-100-two-pointer-explained/