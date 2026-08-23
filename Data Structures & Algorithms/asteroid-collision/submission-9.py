class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                absast = abs(ast)
                if absast == stack[-1]:
                    ast = 0
                    stack.pop()
                elif absast > stack[-1]:
                    stack.pop()
                else:
                    # abs ast is less than current of stack 
                    # so you leave it alone
                    ast = 0
            if ast:
                stack.append(ast)
        return stack

        