class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_to_i = [0] * len(nums)

        for i in range(len(nums)):
            sum_to_i[i] = sum_to_i[i - 1] + nums[i] if i > 0 else nums[i]

        valid_splits = 0
        for x in range(len(nums) - 1):
            if sum_to_i[x] >= sum_to_i[-1] - sum_to_i[x]:
                valid_splits += 1

        return valid_splits

