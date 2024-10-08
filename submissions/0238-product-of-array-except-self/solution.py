class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1]*len(nums)
    #     postfix = [1]*len(nums)

    #     for i in range(1, len(nums)):
    #         prefix[i] = prefix[i - 1] * nums[i - 1]

    #     for i in range(len(nums) - 2, -1, -1):
    #         postfix[i] = postfix[i + 1] * nums[i + 1]


    #     return [a*b for a,b in zip(prefix, postfix)]
            
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(1) space solution??
        output = [1]*len(nums)

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        postfix = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix = postfix * nums[i + 1]
            output[i] = output[i] * postfix

        return output
