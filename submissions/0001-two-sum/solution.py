class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inv_map = {}
        for idx, i in enumerate(nums):
            inv = target - i


            if inv in inv_map:
                return [inv_map[inv], idx]
            else:
                inv_map[i] = idx
            
            
            
            
        
