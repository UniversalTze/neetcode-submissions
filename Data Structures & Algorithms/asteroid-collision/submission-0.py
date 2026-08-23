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
                if val1 > stack[-1]:
                    stack.pop()
                    stack.append(vector)
                elif val1 == stack[-1]:
                    stack.pop()

        return stack
        