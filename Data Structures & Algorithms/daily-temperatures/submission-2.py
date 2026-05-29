class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        # keep track in descending order, if an item is found 
        # to be larger than the top of the stack, keep popping off until
        # you find one that is larger or stack is empty
        # keep index and temperature as you will need it. 
        result = [0] * len(temperatures)
        for index in range(len(temperatures)): 
            if len(stack) == 0:
                # stack is empty
                stack.append((index, temperatures[index]))
            else:
                tup = stack[-1]
                temp = tup[1]
                while temp < temperatures[index]:
                    cur = stack.pop()
                    result[cur[0]] = index - cur[0]
                    if len(stack) == 0:
                        break
                    tup = stack[-1] # keep checking
                    temp = tup[1]
                stack.append((index, temperatures[index]))
        return result



        