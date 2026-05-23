class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # algorithm: -> if all numbers are in sorted descending order (no good time to buy)
        # Intuition: 
        # If you come across a new smaller value, replace it with the current value (new time to buy)
        # if number is bigger than min, we know we can make a profit. 
        # Keep track of previous profit, but if we find a lower value, replace that with min
        # Indicates another potential buying opportunity. 
        # If any prices after that are higher replace new window with new value. 
        min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if min > prices[i]: 
                min = prices[i]
            profit = max(prices[i] - min, profit)
        return profit

        