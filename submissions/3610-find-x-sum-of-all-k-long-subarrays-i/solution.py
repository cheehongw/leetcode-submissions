class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        ans = [0] * (len(nums) - k + 1)

        for i in range((len(nums) - k + 1)):
            
            freq = {}
            for num in nums[i: i + k]:
                freq[num] = freq.get(num, 0) + 1
            
            res = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)
            
            for j in range(min(x, len(res))):
                ans[i] += res[j][0] * res[j][1]
        
        return ans
            

