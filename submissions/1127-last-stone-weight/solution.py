class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapify(stones)


        while(len(stones) > 1):
            h1 = heappop(stones)
            h2 = heappop(stones)
            
            if (h1 == h2):
                continue
            else:
                h1 -= h2
                heappush(stones, h1)
        
        if len(stones):
            return -1 * stones[0]

        else:
            return 0
