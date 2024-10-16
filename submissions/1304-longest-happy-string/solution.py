class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = [x for x in heap if x[0] != 0]

        heapify(heap)

        happyStr = ''


        while heap:
            count, letter = heappop(heap)
            count = -count

            if len(happyStr) >= 2 and happyStr[-1] == letter and happyStr[-2] == letter:
                if heap:
                    count2, letter2 = heappop(heap)
                    count2 = -count2

                    happyStr = happyStr + letter2
                    count2 -= 1
                    if count2 != 0:
                        heappush(heap, (-count2, letter2))
                else:
                    break
            else:
                happyStr = happyStr + letter
                count -= 1
            
            if count != 0:
                heappush(heap, (-count, letter))

        return happyStr

                
            



