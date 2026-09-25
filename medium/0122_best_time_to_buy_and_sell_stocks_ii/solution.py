class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        buy = 0
        while buy < len(prices) - 1:
            if prices[buy] >= prices[buy + 1]:
                buy += 1
                continue

            sell = buy + 1
            while sell < len(prices) - 1 and prices[sell] < prices[sell + 1]:
                sell += 1

            profit += prices[sell] - prices[buy]
            buy = sell

        return profit
