# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_hash = dict()
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in prev_hash:
                return (prev_hash[diff], idx)
            prev_hash[nums[idx]] = idx
