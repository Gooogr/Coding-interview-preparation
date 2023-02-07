# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # store size of subsq for every element
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            # i always before j
            for j in range(i):
                # if nums[i] is part of subsq of nums[j]
                # and counter is less then current max len of subseq
                if nums[i] > nums[j] and dp[i] <= dp[j]: 
                    dp[i] = dp[j] + 1
        return max(dp)