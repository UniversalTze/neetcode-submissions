class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        # at dp[n] which is the goal (there is just one way of getting there)
        # at dp[n-1], there is only just 1 way (1 step up)
        dp[n] = 1
        dp[n - 1] = 1
        curStep = n - 2
        while curStep >= 0:
            dp[curStep] = dp[curStep + 1] + dp[curStep + 2]
            curStep -= 1
        print(dp)
        return dp[0]
        # we are going to move backwards
        