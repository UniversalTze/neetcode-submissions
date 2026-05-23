class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:  # only 1 height in the array so its the max
            return heights[0] * 1
        # use a stack to keep track of smallest area while only keeping track of index
        # index here will be the width of the rectangle
        # the min index will represent the height

        # if heights aren't in increasing order they are popped. 
        # three cases
        # if LHS > RHS: Height cannot be extended, but withd of RHS can be extended back to LHS
        # if LHS < RHS: Height cannot be extended from LHS, but only RHS. Width of LHS can be extended aling with RHS
        # but use RHS as area is larger

        # reasons for the stack
        # only popping the most recent elements and not the ones in the middle (LIFO). 
        WIDTHINDEX = 0
        HEIGHTTUP = 1
        WIDTHONEBOX = 1
        maxarea = 0
        heightindexes = []
        # o(n) time solution

        for index in range(len(heights)):
            popped = False
            area = heights[index] * WIDTHONEBOX # singular case (looking at one height)
            if area > maxarea: 
                maxarea = area
            
            # monotonic stack of indicies and maximum height at time [i].
            if len(heightindexes) == 0:
                heightindexes.append((index, heights[index]))
                continue
            if heights[index] == heightindexes[-1][HEIGHTTUP]: 
                continue
            # wrong logic using how many times was popped. 
            popPrevIndex = 0
            prev = heightindexes[-1]
            print(heightindexes)
            while prev[HEIGHTTUP] > heights[index]:
                popped = True
                popPrevIndex = prev[WIDTHINDEX]
                area = prev[HEIGHTTUP] * (index - prev[WIDTHINDEX])
                if area > maxarea: 
                    maxarea = area
                heightindexes.pop()
                
                if len(heightindexes) == 0: 
                    break
                prev = heightindexes[-1]
                
            if popped: 
                heightindexes.append((popPrevIndex, heights[index]))
            else: 
                heightindexes.append((index, heights[index]))

        lengthOfHeights = len(heights)
        while len(heightindexes) != 0: 
            checkarea = heightindexes.pop()
            area = checkarea[HEIGHTTUP] * (lengthOfHeights - checkarea[WIDTHINDEX])
            maxarea = max(area, maxarea)

        return maxarea
            

        
        