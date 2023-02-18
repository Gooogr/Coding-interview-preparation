# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if num in hash:
                return (hash[num], idx)
            hash[diff] = idx
