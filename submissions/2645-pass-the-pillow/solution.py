class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person = ((time % (2*n - 2)) + 1)
        return person % n if person < n else n - person % n
        
