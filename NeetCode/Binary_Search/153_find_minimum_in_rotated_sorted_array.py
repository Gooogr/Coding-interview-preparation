# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            # if we find minimum sorted part
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            middle = (l + r) // 2
            res = min(res, nums[middle])
            # if we in a rotated (without min) part - go right
            if nums[middle] >= nums[l]:
                l = middle + 1
            # else - go left
            else:
                r = middle - 1
        return res