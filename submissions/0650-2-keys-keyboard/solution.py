class Solution:
    def findFactors(self, n):
        factors = set()
        for i in range(1, ceil(n**0.5) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n // i)
        
        return factors

    memo = {1: 0}
    
    def minSteps(self, n: int) -> int:
        # compute all factors leq n // 2
        if (Solution.memo.get(n) is not None):
            return Solution.memo.get(n)

        factors = self.findFactors(n)
        possible_solns = set()
        for factor in factors:
            if factor <= n // 2:
                possible_soln = self.minSteps(factor) + (n // factor)
                possible_solns.add(possible_soln)
        
        optimal_soln = min(possible_solns)
        Solution.memo[n] = optimal_soln
        return optimal_soln


        
        


        
