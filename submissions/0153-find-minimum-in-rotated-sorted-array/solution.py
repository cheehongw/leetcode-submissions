class Solution:
    # 4 5 6 7 0 1 2 3

    # 0 1 2 3 4 5 6 7


    def findMin(self, nums: List[int]) -> int:
        l_ptr, r_ptr = 0 , len(nums) - 1

        while (r_ptr - l_ptr >= 1):
            mid_point = (l_ptr + r_ptr) // 2

            if (nums[mid_point] < nums[l_ptr]):
                r_ptr = mid_point
            elif (nums[l_ptr] <= nums[mid_point] <= nums[r_ptr]):
                r_ptr = mid_point 
            else:
                l_ptr = mid_point + 1

        return nums[r_ptr]
                
            

        return nums[l_ptr]
