class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach:
        # for each number x in the list, compute the other number y 
        # that will sum up to the target
        # store y in a hashmap so that we can find the idx of x
        # as we iterate through the list, we will eventually encounter the second x
        # that we have hashed into the map as a key
        prevMap = {} 

        for i, n in enumerate(nums):
            diff = target - n
            if n in prevMap:
                return [i, prevMap[n]]
            prevMap[diff] = i

        
            

