class Solution:
    def maxScore(self, nums: List[int]) -> int:

        if not nums:
            return 0
        

        max_factor_score = lcm(*nums) * gcd(*nums)
        
        for i, num in enumerate(nums):
            nums.remove(num)
            LCM = lcm(*nums)
            GCD = gcd(*nums)
            max_factor_score = max(max_factor_score, LCM * GCD)
            nums.insert(i, num)
            
        return max_factor_score
