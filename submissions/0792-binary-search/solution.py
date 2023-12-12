class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = ceil(len(nums)/2)
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if target == nums[pivot]:
            return pivot
        if target < nums[pivot]:
            return self.search(nums[:pivot], target) #pivot exclusive
        else:
            res = self.search(nums[pivot:], target) #pivot inclusive
            return pivot + res if res != -1 else -1
