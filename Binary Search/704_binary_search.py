# https://leetcode.com/problems/binary-search/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left_idx = 0
        right_idx = n - 1

        while left_idx <= right_idx:
            midpoint = left_idx + (right_idx - left_idx) // 2
            midpoint_value = nums[midpoint]
            if midpoint_value == target:
                return midpoint
            elif midpoint_value < target:
                left_idx = midpoint + 1
            else:
                right_idx = midpoint - 1
        return -1
