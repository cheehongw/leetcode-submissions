class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        word_dict = set(dictionary)
        memo = {}

        def dp(i):
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            
            min_extra = 1 + dp(i + 1)

            for x in range(i, len(s)):
                # prefix = s[i: x + 1]
                if s[i: x + 1] in word_dict:
                    min_extra = min(min_extra, dp(x + 1))

            memo[i] = min_extra
            return min_extra
            
        return dp(0)
