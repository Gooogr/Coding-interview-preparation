# https://leetcode.com/problems/contains-duplicate/
# Faster than return len(nums) == len(set(nums))

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev_hash = set()
        for value in nums:
            if value in prev_hash:
                return True
            prev_hash.add(value)
