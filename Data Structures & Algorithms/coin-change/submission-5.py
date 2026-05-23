class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # from 0 -> amount indexes
        # amount indexes will hold value of minimum coins need to reach it
        dparr = [float("inf")] * (amount + 1)

        # there is 0 coins needed to get amount 0
        dparr[0] = 0
        for index in range(1, amount + 1): # O(M * n)-> M is number from 1-target and n is list of coins
            for coin in coins:
                if index - coin < 0:
                    # don't need non negative numbers
                    continue
                dparr[index] = min(dparr[index], dparr[index - coin] + 1)


        
        if dparr[amount] == float("inf"): # base case
            return -1
        return dparr[amount]
        