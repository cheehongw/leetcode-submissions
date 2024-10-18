class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxBitWiseOr = 0

        for i in nums:
            maxBitWiseOr = maxBitWiseOr | i
        

        existingBitwise = 0
        count = 0

        def rec(start):
            nonlocal existingBitwise, count

            if start == len(nums):
                return 0

            temp = existingBitwise
            existingBitwise = nums[start] | existingBitwise
            
            if existingBitwise == maxBitWiseOr:
                remaining = len(nums) - start - 1
                count += 2**remaining
            else:
                rec(start + 1)
            
            existingBitwise = temp
            rec(start + 1)
        
        rec(0)

        return count



        
