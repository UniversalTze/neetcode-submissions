class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures as a stack
        # use a monotonic stack. Pop off elements when something larger has been discovered until 
        # item on stack is larger than current element

        result = [-1] * len(temperatures) # set all to -1 when intialising
        # constants
        DAY = 0
        TEMPERATURE = 1

        # stack used 
        temporder = []

        for day in range(len(temperatures)):
            if len(temporder) == 0: # if empty, then just append tuple
                temporder.append((day, temperatures[day]))  # (DAY, Temp) stored in stack
                continue
            prevHighTemp = temporder[-1][TEMPERATURE]   # check top of stack (should hold elements in descendeing order)
            current = temperatures[day]
            while current > prevHighTemp: 
                update = temporder.pop() # pop when current is higher than item on top of stack
                result[update[DAY]] = day - update[DAY]  # update resulting array
                if len(temporder) == 0: 
                    break
                prevHighTemp = temporder[-1][TEMPERATURE]
            temporder.append((day, temperatures[day]))
        
        # everything remainign in stack needs to be marked with a 0 can pop off or iterate through it
        for temps in range(len(temporder)): 
            update = temporder[temps]
            result[update[DAY]] = 0
        return result