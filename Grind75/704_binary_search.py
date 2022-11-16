# https://leetcode.com/problems/binary-search/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        
        while left_idx <= right_idx:
            midpoint = left_idx + (right_idx - left_idx)//2
            value = nums[midpoint]
            if value == target:
                return midpoint
            elif value < target:
                left_idx = midpoint + 1
            else:
                right_idx = midpoint - 1
        return -1
            