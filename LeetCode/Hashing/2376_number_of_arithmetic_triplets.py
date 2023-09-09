# https://leetcode.com/problems/number-of-arithmetic-triplets/
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # First put all elements in the set, then check we have current - diff and current+ diff in the set.
        counter = 0
        hash = set(nums)
        for idx in range(len(nums)):
            if (nums[idx] - diff in hash) and (nums[idx] + diff in hash):
                counter += 1
        return counter