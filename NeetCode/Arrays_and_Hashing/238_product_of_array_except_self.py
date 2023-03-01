# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# Naive solution with prefix and postfix lists
# Time complexity O(n)
# Space complexity O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # collect prefix and postfix values
        prefix = [1]
        postfix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        for num in nums[::-1]:
            postfix.append(postfix[-1] * num)
        # get final result - multiply values from edges
        res = []
        for idx in range(len(prefix) - 1):
            res.append(prefix[idx] * postfix[len(postfix) - 2 - idx])
        return res


# Inplace approach
# Time complexity O(n) 
# Space complexity O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # left traverse
        p = 1
        for idx in range(len(nums)):
            res[idx] = p
            p *= nums[idx]

        # right traverse
        p = 1
        for idx in range(len(nums) - 1, -1, -1):
            res[idx] *= p
            p *= nums[idx]

        return res
