# https://leetcode.com/problems/3sum-closest

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('inf')
        for idx, val in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            while l < r:
                sum = val + nums[l] + nums[r]
                # If best case
                if sum == target:
                    return target

                # If not best case
                # Update curently best result
                if abs(target - sum) < abs(target - res):
                    res = sum

                # Try to improve next result
                if sum < target:
                    l += 1
                else:
                    r -= 1
        return res