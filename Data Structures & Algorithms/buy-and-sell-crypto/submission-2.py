class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for index in range(1, len(prices)):
            if prices[index] < buy:
                buy = prices[index]
            else:
                profit = max(prices[index] - buy, profit)

        return profit
        