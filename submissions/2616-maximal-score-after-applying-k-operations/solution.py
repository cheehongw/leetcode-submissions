class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        neg_elems = [-v for v in nums]

        heapify(neg_elems)
        score = 0

        for i in range(k):
            max_val = heappop(neg_elems)
            score += -max_val
            heappush(neg_elems, -ceil(-max_val / 3))

        return score

        
        
