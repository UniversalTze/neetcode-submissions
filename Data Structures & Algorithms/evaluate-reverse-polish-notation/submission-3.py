class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens: 
            if token in operators:
                # pop numbers off the stack that need to be performed 
                # in this notatation, it is with two numbers before the notation
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if token == '+': 
                    result = num1 + num2
                elif token == '-':
                    result = num2 - num1
                elif token == '*': 
                    result = num1 * num2
                else: 
                    result = num2 / num1   # floor division
                stack.append(result)
            else: 
                stack.append(token)
        finalres = int(stack.pop())
        return finalres