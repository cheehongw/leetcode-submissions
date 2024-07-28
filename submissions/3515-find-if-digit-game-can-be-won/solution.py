class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sds = 0
        dbl = 0

        for i in nums:
            if i < 10:
                sds += i
            else:
                dbl += i
        

        return sds != dbl
        
