class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sums = []
        MODULO = (10 ** 9) + 7

        for start in range(len(nums)):

            sum = 0
            for length in range(0, len(nums) + 1):
                if (start + length >= len(nums)):
                    continue
                sum += nums[length + start]
                sums.append(sum)

        sums.sort()

        final_sum = 0
        for i in range(left - 1, right):
            # print(i)
            # print(sums)
            final_sum = (final_sum + sums[i]) % MODULO

        return final_sum
                
        
