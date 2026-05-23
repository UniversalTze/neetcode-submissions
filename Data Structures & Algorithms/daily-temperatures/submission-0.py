class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures as a stack
        # use a monotonic stack. Pop off elements when something larger has been discovered until 
        # item on stack is larger than current element

        result = [-1] * len(temperatures)
        DAY = 0
        TEMPERATURE = 1
        temporder = []

        for day in range(len(temperatures)):
            if len(temporder) == 0: 
                temporder.append((day, temperatures[day]))  # (DAY, Temp)
                continue
            prevHighTemp = temporder[-1][TEMPERATURE]
            current = temperatures[day]
            while current > prevHighTemp:
                update = temporder.pop()
                result[update[DAY]] = day - update[DAY]
                if len(temporder) == 0: 
                    break
                prevHighTemp = temporder[-1][TEMPERATURE]
            temporder.append((day, temperatures[day]))
        
        # everything remainign in stack needs to be marked with a 0
        for temps in range(len(temporder)): 
            update = temporder[temps]
            result[update[DAY]] = 0
        return result