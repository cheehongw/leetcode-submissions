class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        memo = [[None] * len(piles) for _ in range(len(piles) + 1)]
        sums = [0] * len(piles)

        sums[len(piles) - 1] = piles[len(piles) - 1]
        for i in range(len(piles) - 2, -1, -1):
            sums[i] = sums[i + 1] + piles[i]


        def stoneGameDp(m, i):

            if (memo[m][i] is not None):
                return memo[m][i]
            
            if (i + 2*m >= len(piles)):
                return sums[i]

            res = 10**7
            for a in range(1, 2*m + 1):
                res = min(res, stoneGameDp(max(a, m), i + a))

            result = sums[i] - res
            memo[m][i] = result

            return result

        return stoneGameDp(1, 0)



        
