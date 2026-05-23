class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # start from a bottum up approach. 

        # From 0 -> amount. Need amount + 1, because amount needs an index in array
        dp = [float("inf")] * (amount + 1)
        # choosing 0 coins is a valid way of making up 0
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0: 
                    # 1 one for the coin denom if its equals 0 or a coin that has been found
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

        