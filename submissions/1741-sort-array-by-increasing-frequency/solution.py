class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0)  + 1

        items = freq.items()
        xs = sorted(items, key=lambda num_freq: (num_freq[1], -num_freq[0]))
        
        res = []
        for num, freq in xs:
            for i in range(freq):
                res.append(num)
        
        return res
