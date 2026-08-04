class MinStack:

    def __init__(self):
        self.stack = []
        self.items = 0
        # this will be a monotonic stack where it holds items in decreasing order.
        self.minstack = []
        self.minstack_items = 0
        

    def push(self, val: int) -> None:
        self.items += 1
        self.stack.append(val)
        if self.minstack_items == 0 or val <= self.minstack[self.minstack_items - 1]:
            self.minstack_items += 1
            self.minstack.append(val)
        
        

    def pop(self) -> None:
        number = self.stack.pop()
        self.items -= 1
        if number == self.minstack[self.minstack_items - 1]:
            self.minstack_items -= 1
            self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[self.items - 1]
        

    def getMin(self) -> int:
        return self.minstack[self.minstack_items - 1]
        
