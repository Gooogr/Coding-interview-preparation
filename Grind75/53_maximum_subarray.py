# https://leetcode.com/problems/maximum-subarray/

from typing import List

# The Kadan's algorithm, O(n) memory and time
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        best_sum = nums[0]
        for idx in range(1, len(nums)):
            # Calculate current contignious sum
            # Will we spild it completely if add new value or not?
            curr_sum = max(nums[idx], curr_sum + nums[idx])
            # Update best result
            best_sum = max(curr_sum, best_sum)
        return best_sum