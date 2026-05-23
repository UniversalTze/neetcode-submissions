class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.size = 0 # used as a window of active things on the stack
        
        """
    def push(self, val: int) -> None:
        if len(self.stack) == self.size: 
            self.stack.append(val)
            if len(self.minstack) == 0: 
                self.minstack.append(val)
            else: 
                minimum = min(val, self.minstack[self.size - 1])
                self.minstack.append(minimum)
            self.size += 1
        else: 
            
            # something has been popped off the stack (accessing stale data)
            self.size += 1 # increment counter first to update needed position
            self.stack[self.size - 1] = val
            minimum = min(val, self.minstack[self.size - 1])
            self.minstack[self.size - 1] = minimum
            
            prev_min = self.minstack[self.size - 1] if self.size > 0 else val
            self.stack[self.size] = val
            self.minstack[self.size] = min(val, prev_min)

        self.size += 1
        """
    def push(self, val: int) -> None:
        if self.size == len(self.stack):
            # Normal append case
            self.stack.append(val)
            if self.size == 0:
                self.minstack.append(val)
            else:
                self.minstack.append(min(val, self.minstack[self.size - 1]))
        else:
            # We are reusing a stale index
            prev_min = self.minstack[self.size - 1] if self.size > 0 else val
            self.stack[self.size] = val
            self.minstack[self.size] = min(val, prev_min)

        self.size += 1
            

    def pop(self) -> None:
        self.size -= 1
        

    def top(self) -> int:
        return self.stack[self.size - 1]
        
    def getMin(self) -> int:
        print(self.size)
        print(self.minstack)
        print(f"min {self.minstack[self.size - 1]}")
        return self.minstack[self.size - 1]
        
