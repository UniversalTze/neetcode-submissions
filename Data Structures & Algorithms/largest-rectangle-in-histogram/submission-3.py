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
        # if equal, the it can continue growing towards the right

        # reasons for the stack (using a monotonic stack)
        # only popping the most recent elements and not the ones in the middle (LIFO). 
        # stack will hold numbers in ascending order when it sees them in array
        # if a number in array is higher than current top of stack
        # stack will be popped (area calculated for max) until  to the proper position 
        # of current index in stack is found. 
        # when proper position is found, the position that was popped off last
        # is kept track off as it indicates the width of current height that are in accordance to the rules

        # e.g as [1, 2, 4, 3]
        # as 4 > 3, 3's histogram can be used to calculate an area of rectangle
        # but 2 < 3, so 2's index cannot be used as its not tall enough to form a rectangle
        # stack = [1, 2, 3] (just heights atm, in reality, use index and height so area can be calcd. )

        WIDTHINDEX = 0
        HEIGHTTUP = 1
        maxarea = 0
        heightindexes = []
        # o(N) time solution
        # o(N) space solution

        for index in range(len(heights)):
            popped = False # for appending to the stack
            
            # monotonic stack of indicies and maximum height at time [i].
            if len(heightindexes) == 0: # nothing in stack so add something to it
                heightindexes.append((index, heights[index]))
                continue
            if heights[index] == heightindexes[-1][HEIGHTTUP]: 
                # if two heights are the same, it can be ignored. Width represents the starting indexes 
                # of a rectangle so that max width can be found
                continue 
            popPrevIndex = 0
            prev = heightindexes[-1]
            print(heightindexes)
            while prev[HEIGHTTUP] > heights[index]:
                popped = True # means we need to current index with historical index
                popPrevIndex = prev[WIDTHINDEX] # keep track of the very last index popped off the stack for max width of current height
                # use the height stored and the max width for that height
                area = prev[HEIGHTTUP] * (index - prev[WIDTHINDEX]) # calculate area to check if its a new max area before discarding it
                if area > maxarea: 
                    maxarea = area
                heightindexes.pop() # remove it from stack
                
                if len(heightindexes) == 0: # if nothing in stack, break out of loop
                    break
                prev = heightindexes[-1] # re-reference the top of stack for next iteration
                
            if popped: 
                # use historical index
                heightindexes.append((popPrevIndex, heights[index]))
            else: 
                # use current index
                heightindexes.append((index, heights[index]))

        lengthOfHeights = len(heights) # number of heights (end of loop)
        # height indexes hold the smallest items that were'nt popped off the stack in iteration 
        # in ascending order. 
        # e.g [1, 3, 5, 2, 5]
        # stack: [(0, 1), (3, 2)] 
        # 1 never popped off as its minimum and should be extendable left or right for area of rectangle
        # 2 is never popped off as 1 is never encountered after. 
        while len(heightindexes) != 0: 
            checkarea = heightindexes.pop()
            # check the minimum multiples to determine max area
            area = checkarea[HEIGHTTUP] * (lengthOfHeights - checkarea[WIDTHINDEX])
            maxarea = max(area, maxarea)

        return maxarea
            

        
        