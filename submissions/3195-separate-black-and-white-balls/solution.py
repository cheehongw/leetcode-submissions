class Solution:
    def minimumSteps(self, s: str) -> int:
        
        count_0 = 0
        ops = 0

        for i in range(len(s)):
            if s[i] == '0':
                ops += (i - count_0)
                count_0 += 1
            
        return ops

            
        
