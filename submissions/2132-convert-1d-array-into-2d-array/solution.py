class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        res = [[None]*n for _ in range(m)]
        
        ptr = 0

        for r in res:
            for j, _ in enumerate(r):
                r[j] = original[ptr]
                ptr += 1

        return res
