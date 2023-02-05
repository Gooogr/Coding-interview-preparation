# https://leetcode.com/problems/partition-equal-subset-sum/

from copy import copy
from typing import List

# iterativly collect all possible sum and caching them
# input - [1, 5, 11, 5] -> target=11
# initialization: set{0} 0 means not added value
# 1 ~ set{0, 1}       
# 5 ~ set{0, 1, 5, 6} 
# 11 ~ set{0, 1, 5, 6, 11, 12, 16, 21} - catch target -> return True

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # handle trivial even cases
        if sum(nums) % 2: 
            return False

        # create chache
        dp = set()
        dp.add(0)

        target = sum(nums) // 2
        for val in nums:
            next_dp = copy(dp)
            for prev_val in dp:
                next_dp.add(val + prev_val)
            dp = next_dp
            if target in dp:
                return True
        return False