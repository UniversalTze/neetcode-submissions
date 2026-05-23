from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        nodesVisited = set()
        nodeQueue = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        # idea is when a "1" has been found do a dfs, but update the grid to "0" after visiting that node
        # so that no extra work is done. 
        # each time this block is entered represents how many islands there is in the map. 
        def bfs(ycoord, xcoord, visited):
            queue = deque([])
            #grid[ycoord][xcoord] = "0" # do it for the first coordinate
            queue.append([ycoord, xcoord])
            check = False
            while queue:
                #print(queue)
                # process the queue until empty
                position = queue.popleft()
                y = position[0]
                x = position[1]
                visited.add(tuple([y,x]))
                for dire in directions:
                    # checks if x and y is in bound and grid[y][x] is 1
                    ynew, xnew = y + dire[0], x + dire[1]
                    if ynew >= ROWS or ynew < 0 or xnew >= COLS or xnew < 0 or grid[ynew][xnew] != "1":
                        continue
                    node = tuple([ynew,xnew])
                    if node in visited:
                        continue
                    queue.append([ynew,xnew])
                    visited.add(node)
                    #grid[ynew][xnew] = "0" # does it for the rest of the coordinates found with 1 that are adjacent
                check = False
        
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    node = tuple([y,x])
                    if node in nodesVisited:
                        continue
                    bfs(y,x, nodesVisited)
                    islands += 1
        return islands
                    


        