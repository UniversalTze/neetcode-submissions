class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.size += 1
        self.stack.append(val)
        if len(self.minstack) == 0:  
            self.minstack.append(val)
        else: 
            minimum = min(val, self.minstack[-1])
            self.minstack.append(minimum)
            print(self.minstack)
        
    def pop(self) -> None: # how to get minimum if popped off stack
        element = self.stack[self.size - 1]
        self.size -= 1
        self.stack = self.stack[0:self.size]
        self.minstack = self.minstack[0:self.size]
        return element

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
