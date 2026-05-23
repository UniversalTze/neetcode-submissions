class Solution:
    def climbStairs(self, n: int) -> int:
        # up to DP

        # can climb up to n using 1 or 2 steps
        # number of distinct way to climb to top of stair case
        # a way of doing is storing the calculated number of way to the stairs using a dictionary

        # base case if i > n:
        # return 0 (as there is no other option of getting n if i > n)

        # base case if i == n:
        # return 1 (as there is no other option of getting n if i > n)
        dp = [0] * (n + 1)
        # 6 elements so that it can go up to index n + 1
        #dp[n] = 1 # store the number of steps to get to N at position n in array
        #dp[n - 1] = 1 # store the number of steps to get to N-1 at position n - 1 in array
        # always the same for different n values. 
        index = n
        while index >= 0:
            if index == n or index == n - 1:
                dp[index] = 1
            else:
                dp[index] = dp[index + 1] + dp[index + 2]
            index -= 1
        return dp[0]


        