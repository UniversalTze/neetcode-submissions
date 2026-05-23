from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        nodeQueue = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        # idea is when a "1" has been found do a dfs, but update the grid to "0" after visiting that node
        # so that no extra work is done. 
        # each time this block is entered represents how many islands there is in the map. 
        def bfs(ycoord, xcoord):
            queue = deque([])
            grid[ycoord][xcoord] = "0"
            queue.append([ycoord, xcoord])
            while queue:
                # process the queue until empty
                position = queue.popleft()
                row = position[0]
                col = position[1]
                for dire in directions:
                    # checks if x and y is in bound and grid[y][x] is 1
                    nr, nc = dire[0] + row, dire[1] + col
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0":
                        continue
                    queue.append([nr,nc])
                    grid[nr][nc] = "0"
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    bfs(y,x)
                    islands += 1
        return islands
                    


        