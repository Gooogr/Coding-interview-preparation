# https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n < 2:
            return dp[n]
        for _ in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])
        return dp[n]