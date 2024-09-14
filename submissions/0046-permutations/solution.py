class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):

            sub_solns = self.permute(nums[:i] + nums[i + 1:])

            for sub_soln in sub_solns:
                res.append([nums[i]] + sub_soln)

        return res
        
