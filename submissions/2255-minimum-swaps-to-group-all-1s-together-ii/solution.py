class Solution:
    
    # O(n) time complexity
    # O(1) space complexity
    # Use a sliding window of size x, where x is the number of 1s
    # - Intuition: Alls ones group together will fit in the sliding window
    # - Find the window with the max number of ones, then we swap the 1s outside the window
    # - to inside the window
    def minSwaps(self, nums: List[int]) -> int:
        
        num_1s = 0
        
        for i in nums:
            if i == 1:
                num_1s += 1
        

        l_ptr = 0
        r_ptr = num_1s
        
        ones_in_windows = 0

        for i in range(l_ptr, r_ptr):
            if nums[i] == 1:
                ones_in_windows += 1
        
        max_ones = ones_in_windows 
        for i in range(len(nums) + 1):
            removed_char = nums[l_ptr]
            l_ptr = (l_ptr + 1) % len(nums)
            ones_in_windows -= removed_char

            new_char = nums[r_ptr % len(nums)]
            r_ptr = (r_ptr + 1) % len(nums)
            ones_in_windows += new_char

            max_ones = max(max_ones, ones_in_windows)
        
        return num_1s - max_ones
            


        
