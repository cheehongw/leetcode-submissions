class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        N = len(nums)

        # for i in range(N - 1, -1, -1):
        #     for j in range(1, N - i):
        #         memo[i] = max(memo[i], (nums[i] * j) + memo[i + j])

        # return memo[0]

        curr_idx = 0
        score = 0
        for idx, num in enumerate(nums):
            if idx == N - 1:
                score += nums[curr_idx] * (idx - curr_idx)

            elif num > nums[curr_idx]:
                score += nums[curr_idx] * (idx - curr_idx)
                curr_idx = idx

        return score


