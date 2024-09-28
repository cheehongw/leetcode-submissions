class MyCircularDeque:

    def __init__(self, k: int):
        # init arr of size K -->
        #            back       
        #           \/
        # [_,_,_,_,_,_,_]
        #      ^ 
        #      front
        # ptrs will point to where front/back elem is.
        # if back == front, then either 1 element exist
        # if front == back == None, then no element exist



        self.size = k
        self.arr = [None] * k
        self.front_ptr = None
        self.back_ptr = None


    def insertFront(self, value: int) -> bool:
        # insert element will move front ptr 'leftwards/counterclockwise'
        if self.isEmpty():
            self.front_ptr = 0
            self.back_ptr = 0
            self.arr[0] = value
            return True
        elif self.isFull():
            return False
        else:
            self.front_ptr = (self.front_ptr - 1) % self.size
            self.arr[self.front_ptr] = value
            return True

    def insertLast(self, value: int) -> bool:
        # insert will move back ptr clockwise
        if self.isEmpty():
            self.front_ptr = 0
            self.back_ptr = 0
            self.arr[0] = value
            return True
        elif self.isFull():
            return False
        else:
            self.back_ptr = (self.back_ptr + 1) % self.size
            self.arr[self.back_ptr] = value
            return True

    def deleteFront(self) -> bool:
        # move front_ptr clockwise
        if self.isEmpty():
            return False
        
        if self.front_ptr is not None and self.front_ptr == self.back_ptr:
            self.front_ptr = None
            self.back_ptr = None
            return True
        
        self.front_ptr = (self.front_ptr + 1) % self.size
        return True

        

    def deleteLast(self) -> bool:
        # move back_ptr anti clockwise
        if self.isEmpty():
            return False
        
        if self.back_ptr is not None and self.front_ptr == self.back_ptr:
            self.front_ptr = None
            self.back_ptr = None
            return True
        
        self.back_ptr = (self.back_ptr - 1) % self.size
        return True

    def getFront(self) -> int:
        if self.front_ptr is not None:
            return self.arr[self.front_ptr]
        else:
            return -1
        

    def getRear(self) -> int:
        if self.back_ptr is not None:
            return self.arr[self.back_ptr]
        else:
            return -1
                

    def isEmpty(self) -> bool:
        return self.back_ptr is None and self.front_ptr is None
        

    def isFull(self) -> bool:
        #deque is full if front_ptr is to the 'right/clockwise' of back_ptr
        if (self.back_ptr is not None and self.front_ptr is not None):
            return (self.back_ptr + 1) % self.size == self.front_ptr
        
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
