# https://leetcode.com/problems/remove-element/

from typing import List

# My solution with O(n) complexity and O(1) memory
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            # find target in left part
            while nums[l] != val and l < r:
                l += 1
            # find vacant place in right part
            while nums[r] == val and l < r:
                r -= 1
            # swap elements
            nums[l], nums[r] = nums[r], nums[l] 
        # count amount of non-target values
        return len(nums) - nums.count(val)

# Faster code with only one while loop.
# But the idea is the same
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        val_counter = 0
        while l <= r:
            if nums[l] != val:
                l +=1
            elif nums[r] == val:
                val_counter += 1
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                val_counter += 1
        return len(nums) - val_counter