class MinStack:

    def __init__(self):
        # no using pop
        self.stack = []
        self.minstack = []
        self.size = 0
        
    def push(self, val: int) -> None:
        if self.size == len(self.stack): 
            # normal append to end of stack as they are in sync
            self.stack.append(val)
            if self.size == 0: # no current minimum as of yet
                self.minstack.append(val)
            else: 
                # find minimum of current value being added and last active minimum value
                # (derived from size of current window on stack)
                minimum = min(val, self.minstack[self.size - 1])
                self.minstack.append(minimum)
        else: 
            # something has been popped off the stack so it is out of sync. 
            # example: push -3, push -2 push -1 
            # [-3, -2, -1], size = 3. Stack.pop() (min stack): [-3, -3, -3]
            # [-3, -2 |, -1] size = 2 (| indicates active window after pop). Last index should be 1 (size - 1)
            # minstack: [-3, -3 |, -3]
            # therefore when updating, just use size as index to be updated rather than size - 1.
            # size currently holds the beginning index of stale data that can be updated. 
            self.stack[self.size] = val
            # grab the last active minimum index
            prevMin = self.minstack[self.size - 1] if self.size > 0 else val
            self.minstack[self.size] = min(prevMin, val)
        self.size += 1

    def pop(self) -> None:
        self.size -= 1
        # no using .pop()

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.minstack[self.size - 1]
        
