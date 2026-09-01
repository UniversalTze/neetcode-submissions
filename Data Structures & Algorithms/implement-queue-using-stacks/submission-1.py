class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.peekval = 0
        

    def push(self, x: int) -> None:
        if self.empty():
            self.peekval = x
        self.stack1.append(x)
        

    def pop(self) -> int:
        while len(self.stack1) != 1:
            val = self.stack1.pop()
            self.stack2.append(val)
        
        finalval = self.stack1.pop()
        self.peekval = self.stack2[-1] if len(self.stack2) else 0
        while len(self.stack2) > 0:
            value = self.stack2.pop()
            self.stack1.append(value)

        return finalval


    def peek(self) -> int:
        return self.peekval
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()