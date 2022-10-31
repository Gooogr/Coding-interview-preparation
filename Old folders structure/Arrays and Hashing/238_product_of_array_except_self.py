# https://leetcode.com/problems/product-of-array-except-self/
# Complexity O(n), Memory O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        p = 1
        
        # Find products to the left from every element
        for idx in range(len(nums)):
            result[idx] = p
            p *= nums[idx]
            
        # Find products to the right from every element. 
        # Multiply to the sub-results from the previous iteration
        p = 1
        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= p
            p *=  nums[idx]
        return result
