class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for vector in asteroids: 
            if len(stack) == 0:
                stack.append(vector)
            elif vector > 0:
                stack.append(vector)
            else:
                # vector is negative 
                val1 = abs(vector)
                val2 = stack[-1]
                if val1 == val2: 
                    stack.pop()
                else:
                    while val1 > val2 and len(stack) != 0:
                        # stack only holds positive numbers
                        stack.pop()
                        val2 = stack[-1]
                    if len(stack) == 0:
                        # all has been popped except this negative number
                        stack.append(vector)
                    
        return stack
        