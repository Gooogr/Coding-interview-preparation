# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_idx = 0
        for sell_idx in range(len(prices)):
            # if it's profit step - get this profit
            # if it's not - skip and wait for better price
            if prices[sell_idx] > prices[buy_idx]:
                max_profit += prices[sell_idx] - prices[buy_idx]
            # update buy_idx for next step
            buy_idx = sell_idx
        return max_profit