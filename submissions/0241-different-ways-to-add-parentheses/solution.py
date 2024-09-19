class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        # 2 - 1 - 1
        # 2 - (1 - 1)
        # (2 - 1) - 1

        # dp(2 * 3 - 4 * 5) = [2 * dp(3 - 4 * 5)].extend([dp(2 * 3 - 4) * 5]) == [-34, -10, -10, 10]

        # dp(3 - 4 * 5) = 3 - dp(4*5) and dp(3-4) * 5 == [-17, -5]
        # dp(2 * 3 - 4) = 2 * dp(3-4) and dp(2*3) - 4 == [-2, 2]
        
        
        memo = [[None] * (len(expression)+1) for _ in range(len(expression) + 1)]


        def dp(start_incl, end_excl):
            
            if (memo[start_incl][end_excl]):
                return memo[start_incl][end_excl]

            if end_excl - start_incl <= 2:
                memo[start_incl][end_excl] = [int(expression[start_incl:end_excl])]
                return memo[start_incl][end_excl]

            res = []
            for i in range(start_incl, end_excl):
                c = expression[i]
                
                if c != '+' and c != '-' and c != '*':
                    continue
                
                operator = c
                left = dp(start_incl, i)
                right = dp(i + 1, end_excl)

                if operator == '+':
                    res.extend([x + y for x in left for y in right])
                if operator == '-':
                    res.extend([x - y for x in left for y in right])
                if operator == '*':
                    res.extend([x * y for x in left for y in right])

            memo[start_incl][end_excl] = res

            return res

        return dp(0, len(expression))
