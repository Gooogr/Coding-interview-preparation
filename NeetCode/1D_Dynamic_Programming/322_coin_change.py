# https://leetcode.com/problems/coin-change/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp - min amount of coins to get sum in [0..amount]
        dp = [1e9] * (amount + 1)
        dp[0] = 0 
        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    # dp[i] = 1 + dp[i - coin] but min track count history!
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        return dp[amount] if dp[amount] < 1e9 else -1