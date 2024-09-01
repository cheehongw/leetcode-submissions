class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        maxHeap = []
        res = []
        
        for q in queries:
            x, y = q[0], q[1]
            dis = abs(x) + abs(y)
            
            heappush(maxHeap, -dis)
            if (len(maxHeap) < k):
                res.append(-1)
            else:
                while len(maxHeap) > k:
                    heappop(maxHeap)

                k_nearest = maxHeap[0]
                res.append(-k_nearest)

        return res

        
