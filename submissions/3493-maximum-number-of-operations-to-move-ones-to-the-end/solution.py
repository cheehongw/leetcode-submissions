class Solution:
    def maxOperations(self, s: str) -> int:
        
        ones_encountered = 0
        ops = 0
        for i in range(len(s)):
            if (s[i] == '1'):
                ones_encountered += 1
            else:
                if i-1 >= 0 and s[i - 1] == '1':
                    #gap detected
                    ops += ones_encountered
        
        return ops





