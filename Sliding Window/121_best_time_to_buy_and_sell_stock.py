# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # buy_idx - buy point, cell_idx - cell point
        buy_idx = 0

        for cell_idx in range(1, len(prices)):
            # If we found cheaper buy point - use it
            if prices[buy_idx] > prices[cell_idx]:
                buy_idx = cell_idx
            # Find current profit and compare it with maximum profit
            profit = prices[cell_idx] - prices[buy_idx]
            max_profit = max(max_profit, profit)
        return max_profit