# https://leetcode.com/problems/daily-temperatures/

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # for pairs [temperature, index]
        
        for idx, temp in enumerate(temperatures):
            # find the first occured temperature that bigger than current 
            while stack and temp > stack[-1][0]:
                _, stack_idx = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append([temp, idx])
        return result