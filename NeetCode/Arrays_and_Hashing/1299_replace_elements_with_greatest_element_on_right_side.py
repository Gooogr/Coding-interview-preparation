# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

from typing import List

# My solution, with O(n) memory and O(n) complexity
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        result[-1] = -1
        current_max = -1 * float('inf')
        # iterate back from beggining and update current max of right slice
        for idx in range(len(arr) - 1, 0, -1):
            current_max = max(arr[idx], current_max)
            result[idx - 1] = current_max
        return result

# In-place solution with O(1) memory and O(n) complexity
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1 
        # iterate back from beggining and update current max of right slice
        for idx in range(len(arr) - 1, -1, -1):
            current_max = max(arr[idx], right_max)
            arr[idx] = right_max
            right_max = current_max
        return arr
