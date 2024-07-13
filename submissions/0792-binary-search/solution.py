class Solution:
    def search(self, nums: List[int], target: int) -> int:
        point = len(nums) // 2
        
        if len(nums) == 0:
            return -1

        while (True):
            if (nums[point] == target):
                return point
            elif (target < nums[point]):
                return self.search(nums[:point], target)
            else:
                result = self.search(nums[point + 1:], target) 
                return result if result == -1 else result + point + 1
