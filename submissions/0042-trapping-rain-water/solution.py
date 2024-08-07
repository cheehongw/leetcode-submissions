class Solution:

    def trap(self, height: List[int]) -> int:
        l_max = [0]*len(height)
        r_max = [0]*len(height)

        max_left = 0
        for i,h in enumerate(height):
            l_max[i] = max_left
            max_left = max(max_left, h)
        
        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            r_max[i] = max_right
            max_right = max(max_right, height[i])
        
        trapped = 0

        for i,h in enumerate(height):
            t = max(min(l_max[i], r_max[i]) - h, 0)
            trapped += t

        return trapped
            


            
            





        
