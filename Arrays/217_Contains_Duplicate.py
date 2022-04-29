# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## Slower one-liner
        # return not len(nums) == len(set(nums))
        
        ## Faster iteration
        hashset = set()
        for item in nums:
            if item not in hashset:
                hashset.add(item)
        return not len(nums) == len(hashset)
