class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy = list(set(arr))
        copy.sort()
        
        rankings = {}

        curr_rank = 1
        
        for x in copy:
            rankings[x] = curr_rank
            curr_rank += 1
        
        res = [None]*len(arr)

        for i,x in enumerate(arr):
            res[i] = rankings[x]

        return res
        



