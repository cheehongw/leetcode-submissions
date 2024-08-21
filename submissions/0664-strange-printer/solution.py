class Solution:
    def strangePrinter(self, s: str) -> int:
        str_len = len(s)

        memo = {}

        def minPrints(i, j):
            if i > j:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            min_turns = 1 + minPrints(i + 1, j)

            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    turns = minPrints(i, k -1) + minPrints(k+1, j)
                    min_turns = min(min_turns, turns)

            memo[(i,j)] = min_turns

            return min_turns
        
        return minPrints(0, str_len - 1)


        

        
