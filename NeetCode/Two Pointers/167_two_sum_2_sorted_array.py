# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Optimal O(n)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l_idx = 0
        r_idx = len(numbers) - 1
        while l_idx < r_idx:  # or just while True, becasue we were garanteed to have solution
            l_value = numbers[l_idx]
            r_value = numbers[r_idx]
            result = l_value + r_value
            if result == target:
                return [l_idx + 1, r_idx + 1]  # task demand to add this +1. I don't know why
            elif result < target:
                l_idx += 1
            else:
                r_idx -= 1


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