class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for vector in asteroids:
            print(stack)
            if len(stack) == 0:
                stack.append(vector)
            elif vector < 0 and abs(vector) == stack[-1]:
                stack.pop()
            else:
                value = stack[-1]
                if (value > 0 and vector < 0):
                    while len(stack) != 0 and (value > 0 and vector < 0):
                        val2 = abs(vector)
                        if val2 > value:
                            stack.pop()
                            value = stack[-1]
                        else:
                            break
                    if value < 0:
                        # if its a negative number found and current vector is negative
                        # append to stack
                        # if value was positive, it just means that a larger positive 
                        # number was found
                        # causing negative to be destroyed
                        stack.append(vector)
                else:
                    stack.append(vector)
        
        return stack
        