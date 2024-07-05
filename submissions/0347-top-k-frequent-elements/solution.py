class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        freq = collections.defaultdict(list)
        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for key, val in counts.items():
            freq[val].append(key)
        

        res = []
        for i in range(len(nums), 0, -1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) == k:
                    return res

