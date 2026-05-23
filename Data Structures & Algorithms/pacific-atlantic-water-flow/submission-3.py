class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
         # understand that the bottom left corner and top right corner is both 
        # atlantic and pacific. 
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        # create seen sets for both pacific and atlantic
        res = [] # final result
        # picking DFS to run on specific cells. While storing the nodes 
        # you've visited. When visited you can tell the DFS to stop looking. 
        # instead of going from where water can flow, we go from the edges 
        # and use where water can come from (hence picking the edges where
        # it is equal to or larger than current height).
        def dfs(row, column, prevHigh, seenSet):
            # bounds check
            if row < 0 or column < 0 or row >= ROWS or column >= COLS:
                return
            # Check if node has been explored or first the condition where we 
            # are finding where water flows from (starting at the edges of pacific and atlantic)
            coord = (row, column)
            if heights[row][column] < prevHigh or coord in seenSet:
                return
            seenSet.add(coord)
            if heights[row][column] > prevHigh:
                prevHigh = heights[row][column]
            dfs(row + 1, column, prevHigh, seenSet)
            dfs(row - 1, column, prevHigh, seenSet)
            dfs(row, column + 1, prevHigh, seenSet)
            dfs(row, column - 1, prevHigh, seenSet)
        # prev high is 0 for all dfs at the beginning. 
        prevHigh = 0
        for col in range(COLS):
            dfs(0, col, 0, pac)
            dfs(ROWS - 1, col, 0, atl)

        for row in range(ROWS):
            dfs(row, 0, 0, pac)
            dfs(row, COLS - 1, 0, atl)

        for row in range(ROWS):
            for col in range(COLS):
                coord = (row, col)
                if coord in atl and coord in pac:
                    res.append(list(coord))

        return res
        