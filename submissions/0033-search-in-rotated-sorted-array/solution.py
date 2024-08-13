class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_ptr, r_ptr = 0, len(nums) - 1

        while (l_ptr <= r_ptr):
            midpoint = (l_ptr + r_ptr) // 2

            # print(l_ptr, midpoint, r_ptr)

            m = nums[midpoint]
            l = nums[l_ptr]
            r = nums[r_ptr]

            if target == m:
                return midpoint

            if target == l:
                return l_ptr
            
            if target == r:
                return r_ptr

            if (l < m and l < target < m):
                r_ptr = midpoint - 1
            elif (m < r and m < target < r):
                l_ptr = midpoint + 1
            elif (m > r and (target < r or target > m)):
                l_ptr = midpoint + 1
            elif (l > m and (target < m or target > l)):
                r_ptr = midpoint - 1
            else:
                break
        
        return -1


