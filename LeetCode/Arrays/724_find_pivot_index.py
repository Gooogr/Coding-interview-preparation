# https://leetcode.com/problems/find-pivot-index

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        for idx, value in enumerate(nums):
            tmp_sum = right_sum - value
            if left_sum == tmp_sum:
                return idx
            left_sum += value
            right_sum -= value
        return -1