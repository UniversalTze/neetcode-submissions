class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        # m represents number of rows
        # n represents number of columns
        TOPLEFT = 0
        # brute force -> at each point use pathfinding to see if you can get to desired location
        # if so add that to running total. (starting from the top down to bottom).

        # optimised path -> use backtracking dp. Understand that the ones directly to the left of the desired location
        # and above the desired location, there is just 1 way of getting there. In this case, we can only
        # move right and down. But left of the desired location and above the desired location represent this case
        # for the first iteration. The position that is diagonal of the x, will use these first values to calculate
        # how many possible ways there is from getting x. In this case, you can move down (1) and right (1), which at this
        # location y, you have two ways. This recursive way of solving it will keep going back until you get to top right
        # corner. So 2DP is used to calculate how ways you can get from tiles closest and to the left and above from x,
        # and backtrack our way using the solutions to these problems until we get to the top left corner


        dptwoArr = [[0] * n for _ in range(m)]
        # understand that items on the boundaries can move one direction so we set the boundaries
        # these boundaries are for when columns = n - 1 (can only move down)
        # or when rows = m - 1 (can only move right)

        dptwoArr[m - 1][n - 1] = 1
        rows = m
        cols = n
        for row in range(rows - 1, -1 , -1):
            for column in range(cols - 1, -1, -1):
                if row == m - 1 or column == n - 1:
                    dptwoArr[row][column] = 1
                else:
                    dptwoArr[row][column] = dptwoArr[row + 1][column] + dptwoArr[row][column + 1]
        return dptwoArr[TOPLEFT][TOPLEFT]
        """

        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]

        return dp[0]
        