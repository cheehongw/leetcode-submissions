class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(height) - 1

        curr_max_water = min(height[l_ptr], height[r_ptr])*(r_ptr - l_ptr)

        while (l_ptr < r_ptr):
            water_area = min(height[l_ptr], height[r_ptr])*(r_ptr - l_ptr)
            curr_max_water = max(water_area, curr_max_water)

            if (height[l_ptr] < height[r_ptr]):
                l_ptr += 1
            else:
                r_ptr -= 1
        
        return curr_max_water
