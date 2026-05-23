class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        if amount == 0: # choosing 0 is a valid way to make up 0
            return 0
        # will explicitly state if coins are in order, else assume not. 
        # using a map of coins and numbers left to retrieve the target
        # going by the idea that coins is ordered, assuming that largerst coin is at the end.
        # wrong idea, now that we know that coins are unordered. 
        minCoins = -1
        coinMap = {0: minCoins}
        curIndex = 0
        while curIndex < len(coins):
            goal = amount
            numOfCoins = 0
            denomCoin = coins[curIndex]
            currentCount = 0
            while currentCount <= goal:
                currentCount += denomCoin
                numOfCoins += 1
                difference = goal - currentCount
                if difference not in coinMap:
                    coinMap[difference] = numOfCoins
                # means taht current coin is in coin map
                else:
                    # current count holds the amount need to match target
                    # this is the difference that sums to goal
                    coinsTaken = coinMap[difference]
                    if coinsTaken == -1 or coinsTaken > numOfCoins:
                        coinMap[difference] = numOfCoins
                    if goal - difference in coinMap:
                        toadd = coinMap[goal - difference]
                        coinMap[0] = min(coinMap[0], toadd + numOfCoins)
            curIndex += 1
        print(coinMap)
        return -1 if coinMap[0] == -1 else coinMap[0] 
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
            
        
        