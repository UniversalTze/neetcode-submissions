class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time and O(n) space
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        if len(s) == 1:  # no matching closing bracket as its just one char
            return False
        for char in s: 
            if char == '(' or char == '{' or char == '[': 
                # if opening bracket, push the closing bracket that should be returned if not an opening bracket
                # stack keeps track of most recent bracket opening
                # and ensures that next character should be the closing if that's the case
                stack.append(char) 
            else:
                if len(stack) == 0 or char != brackets[stack.pop()]: 
                    # check that current char is the closing bracket of most recent opening bracket
                    # kept track by using the stack
                    return False
    
        if (len(stack)) > 0: # opening brackets don't have closing brackets with them...
            return False
        return True
        