class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # so classic DP problem. Very similar to house of robbers
        goal = len(cost) - 1
        dp = [0] * (goal + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for index in range(2, goal + 1):
            if index + 1 > goal: 
                dp[index] = min(dp[index - 1], dp[index - 2] + cost[index])
            else: 
                dp[index] = min(dp[index - 1] + cost[index], dp[index - 2] + cost[index])
        
        if len(cost) == 2:
            return min(dp[0], dp[1])
        return dp[goal]
        