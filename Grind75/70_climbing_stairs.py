# https://leetcode.com/problems/climbing-stairs

# Recusrive approach
class Solution:
    def climbStairs(self, n: int) -> int:
        def count_ways(n, memo=dict()):
            if n < 2:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = count_ways(n-1, memo) + count_ways(n-2, memo)
            return memo[n]
        return count_ways(n)
    
# Iterative Fibonachi-like approach without memory
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        curr = 2
        for _ in range(3, n + 1):
            tmp = prev + curr
            prev = curr
            curr = tmp
        return curr

# Iterative approach with memory
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for idx in range(2, n + 1):
            dp[idx] = dp[idx-1] + dp[idx-2]
        return dp[n]
