class Solution:
    def findScore(self, nums: List[int]) -> int:

        pq = []

        for idx, num in enumerate(nums):
            heappush(pq, (num, idx))
        
        marked = set()

        score = 0
        while pq:
            num, idx = heappop(pq)
            if (idx not in marked):
                marked.add(idx)
                marked.add(idx - 1)
                marked.add(idx + 1)
                score += num
            
        return score
