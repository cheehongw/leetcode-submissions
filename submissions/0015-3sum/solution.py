class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        a = None
        for idx, num in enumerate(nums):
            if num == a:
                continue
            
            a = num
            l_ptr = idx + 1
            r_ptr = len(nums) - 1
            target = 0 - num

            while (l_ptr < r_ptr):
                if nums[l_ptr] + nums[r_ptr] == target:
                    res.append([num, nums[l_ptr], nums[r_ptr]])
                    temp = nums[l_ptr]
                    while(l_ptr < r_ptr and nums[l_ptr] == temp):
                        l_ptr += 1
                
                elif nums[l_ptr] + nums[r_ptr] > target:
                    r_ptr -= 1
                
                else:
                    l_ptr += 1

        return res
                    
            
