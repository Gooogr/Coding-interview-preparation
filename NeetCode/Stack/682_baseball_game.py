# https://leetcode.com/problems/baseball-game/

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for item in operations:
            if item.lstrip("-").isnumeric():
                stack.append(int(item))
            elif item == '+':
                prev_sum = int(stack[-1]) + int(stack[-2])
                stack.append(prev_sum)
            elif item == 'D':
                double = int(stack[-1]) * 2
                stack.append(double)
            elif item == 'C':
                stack.pop()
        print(stack)
        return sum(stack)