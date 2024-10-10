class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        maxWidth = 0

        for i in range(len(nums) - 1, -1, -1):
            while(stack and nums[i] >= nums[stack[-1]]):
                maxWidth = max(maxWidth, i - stack[-1])
                stack.pop()
        
        return maxWidth


        
