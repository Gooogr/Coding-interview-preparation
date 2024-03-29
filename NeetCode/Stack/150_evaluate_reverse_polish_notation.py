# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

# Polish notation assume that any sign apply only to the last two digits
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else: # because str.isdigit can't handle negative values like "-11"
                stack.append(int(token))
        return stack[0]