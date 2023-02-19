# https://leetcode.com/problems/contains-duplicate-ii

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = dict()
        for idx, val in enumerate(nums):
            # find diff between two most recent indicies of repeated value
            if val in hash_table and abs(idx - hash_table[val]) <= k:
                return True
            hash_table[val] = idx