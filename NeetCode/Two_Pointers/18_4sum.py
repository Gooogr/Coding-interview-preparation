# https://leetcode.com/problems/4sum/

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for idx1 in range(len(nums)):
            # skip repeated values
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                continue
            for idx2 in range(idx1 + 1, len(nums)):
                if idx2 > idx1 + 1 and nums[idx2] == nums[idx2 - 1]:
                    continue
                # And now solve 2 sum for sorted array
                l = idx2 + 1
                r = len(nums) - 1
                while l < r:
                    summ = nums[idx1] + nums[idx2] + nums[l] + nums[r]
                    if target == summ:
                        result.append([nums[idx1], nums[idx2], nums[l], nums[r]])
                        l += 1
                        # skip duplicates
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                    elif target > summ:
                        l += 1
                    else:
                        r -= 1
        return result