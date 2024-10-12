class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        target_nums = {}

        for i in nums:
            target_nums[i] = -1

        
        for i in range(1000):
            res = i | i + 1

            if res in target_nums and target_nums[res] == -1:
                target_nums[res] = i
        
        sol = [-1] * len(nums)
        for idx, num in enumerate(nums):
            sol[idx] = target_nums[num]

        return sol

        
        
