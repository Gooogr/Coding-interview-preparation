# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for idx, val1 in enumerate(nums):
            # handle repeated triplets
            if idx > 0 and val1 == nums[idx - 1]:
                continue
            # solve 2sum problem for sorted list
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                summ = nums[l] + nums[r] + val1
                if summ == 0:
                    result.append([val1, nums[l], nums[r]])
                    # push pointer further and skip duplets
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif summ < 0:
                    l +=1
                else:
                    r -=1
        return result