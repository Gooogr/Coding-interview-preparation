# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List

# Recusrive approach with memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def rec_min(i: int, cost: List[int]=cost, memo: dict={}):
            if i < 0: return 0
            if i < 2: return cost[i]
            if i in memo: return memo[i]
            memo[i] = cost[i] + min(rec_min(i - 1, memo=memo), rec_min(i - 2, memo=memo))
            return memo[i]
        n = len(cost)
        return min(rec_min(n - 1), rec_min(n - 2))

# Tabulation approach with O(n) space complexity
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # where 2 <= cost.length <= 1000
        dp = [None] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for step in range(2, n):
            dp[step] = cost[step] + min(dp[step - 1], dp[step - 2])
        return min(dp[n - 1], dp[n - 2])

# Tabulation approach with O(1) space complexity
# We need only two last minimal values: i-1 and i - 2
# So, like in Fibonacci numbers:
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) # 2 <= cost.length <= 1000
        one_step = cost[0]
        two_step = cost[1]
        for step in range(2, n):
            curr = cost[step] + min(one_step, two_step)
            one_step = two_step
            two_step = curr
        return min(one_step, two_step)

