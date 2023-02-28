# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List

# Optimal solution without additional memory
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            temp_sum = numbers[l] + numbers[r]
            if temp_sum == target:
                return [l + 1, r + 1] # +1 because leetcode demands it
            elif temp_sum > target:
                r -= 1
            else:
                l += 1

# Non-optimal solution, just typical 2 sum with hash
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_values = dict()
        n = len(numbers)
        for idx in range(n):
            diff = target - numbers[idx]
            if diff in hash_values:
                return (hash_values[diff] + 1, idx + 1) #add +1 as task demand
            else:
                hash_values[numbers[idx]] = idx