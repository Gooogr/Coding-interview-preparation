# https://leetcode.com/problems/asteroid-collision/

from typing import List

# collison condition:
#  X[i-1] > 0 and X[i] < 0 => ... 0-> <-0 ...

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and (a < 0) and (stack[-1] > 0): #catch collision
                diff = a + stack[-1]
                if diff < 0: # new break old and replace it
                    stack.pop()
                elif diff > 0: # old survive and break new
                    a = 0 # stop loop and skip this value later
                else: # both destroyed
                    stack.pop()
                    a = 0
            if a: #skip zeroes
                stack.append(a)
        return stack
                    