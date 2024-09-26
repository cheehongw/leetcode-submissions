class MyCalendar:

    def __init__(self):
        self.bookings = [-1, -1, 10**9 + 1, 10**9 + 2]
        

    def book(self, start: int, end: int) -> bool:
        
        for i in range(len(self.bookings)):
            if start < self.bookings[i] and end <= self.bookings[i] and start >= self.bookings[i - 1] and end > self.bookings[i - 1]:
                if i % 2 == 0:
                    self.bookings.insert(i, end)
                    self.bookings.insert(i, start)
                    return True
                else:
                    return False
            



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
