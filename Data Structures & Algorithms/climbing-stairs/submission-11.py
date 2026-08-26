class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        # if n is 3 = [0, 0, 0, 0]
        dp[0] = 1 # one way to current position
        dp[1] = 1 # only way to get to step 1 (move 1 step up)
        for index in range(2, n + 1):
            dp[index] = dp[index - 1] + dp[index - 2]
        return dp[n]
        