# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr # invert order from stack
                stack.pop()                       # remove '['

                coef = ''
                while stack and stack[-1].isnumeric():
                    coef = stack.pop() + coef
                stack.append(int(coef) * substr)
        return "".join(stack)