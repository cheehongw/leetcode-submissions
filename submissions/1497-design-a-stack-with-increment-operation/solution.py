class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = [None]*maxSize
        # ptr will point to the next empty spot in the stack
        self.ptr = 0
        

    def push(self, x: int) -> None:
        if self.ptr != len(self.arr):
            self.arr[self.ptr] = x
            self.ptr += 1
        

    def pop(self) -> int:
        if (self.ptr == 0):
            return -1
        
        self.ptr -= 1
        return self.arr[self.ptr]
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.ptr)):
            self.arr[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
