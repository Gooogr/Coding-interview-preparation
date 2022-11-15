# https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hash = {}
        for idx, value in enumerate(nums):
            diff = target - value
            # We have current X. 
	    # Have we already met Y that X + Y = target?
            if diff in prev_hash:
                return [prev_hash[diff], idx]  
            prev_hash[value] = idx
