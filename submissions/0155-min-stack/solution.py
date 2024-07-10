from heapq import *

class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None
        
    def push(self, val: int) -> None:
        if (self.curr_min is None):
            self.stack.append((val, val))
            self.curr_min = val
        else:
            self.curr_min = val if val < self.curr_min else self.curr_min
            self.stack.append((val, self.curr_min))

    def pop(self) -> None:
        self.stack.pop()
        self.curr_min = self.stack[-1][1] if len(self.stack) > 0 else None

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
