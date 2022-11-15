# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_point = 0
        max_profit = 0
        for sell_point in range(1, len(prices)):
            # if we find cheaper buy pointer - use it
            if prices[sell_point] < prices[buy_point]:
                buy_point = sell_point
            # find biggest profit for current buy point
            profit = prices[sell_point] - prices[buy_point]
            max_profit = max(profit, max_profit)
        return max_profit