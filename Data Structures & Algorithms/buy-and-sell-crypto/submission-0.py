class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # algorithm: -> if all numbers are in sorted descending order (no good time to buy)
        # everytime min resets (find minimum) -> if there is a number higher than it sell. 
        # (won't work for every case given [1, 6, 0, 4])
        # two pointer approach with one representing the beginning of window, and the the other one is the end
        min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if min > prices[i]: 
                min = prices[i]
            profit = max(prices[i] - min, profit)
        return profit

        