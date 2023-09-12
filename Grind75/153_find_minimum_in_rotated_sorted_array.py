# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # if we are in left rotated part - move left border to right + 1
            if nums[m] > nums[r]:
                l = m + 1
            # if we are in right non-rotated part - keep right border
            else:
                r = m
        return nums[l]