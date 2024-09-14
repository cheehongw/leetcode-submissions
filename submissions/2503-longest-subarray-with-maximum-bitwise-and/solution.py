class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest_AND = 0
        longest_contiguous = 0
        
        curr_length = 0
        for i, n in enumerate(nums):
            if (n > largest_AND):
                largest_AND = n
                longest_contiguous = 0
                curr_length = 0

            if n == largest_AND:
                curr_length += 1
                longest_contiguous = max(longest_contiguous, curr_length)
            else:
                curr_length = 0

        return longest_contiguous
