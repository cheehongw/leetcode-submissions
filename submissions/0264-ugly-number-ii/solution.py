class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        i2, i3, i5 = 0, 0, 0
        next_mult_2, next_mult_3, next_mult_5 = 2, 3, 5
        ugly_nums = [0] * 1690
        ugly_nums[0] = 1
        c = 1

        while (c < n):
            next_ugly_num = min(ugly_nums[i2] * 2, ugly_nums[i3]*3, ugly_nums[i5]*5)
            ugly_nums[c] = next_ugly_num
            c += 1

            if next_ugly_num == next_mult_2:
                i2 += 1
                next_mult_2 = ugly_nums[i2] * 2
            if next_ugly_num == next_mult_3:
                i3 += 1
                next_mult_3 = ugly_nums[i3] * 3            
            if next_ugly_num == next_mult_5:
                i5 += 1
                next_mult_5 = ugly_nums[i5] * 5
        

        return ugly_nums[n - 1]
         
        
