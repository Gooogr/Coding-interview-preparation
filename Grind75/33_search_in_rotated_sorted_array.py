# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # middle pointer in left-side part
            if nums[l] <= nums[m]:
                # if target in rotated right part or just bigger then left limit
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            # middle pointer in right-side part
            else:
                # if target in non-rotated left part or just less than right limit
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m +1
        return -1
        