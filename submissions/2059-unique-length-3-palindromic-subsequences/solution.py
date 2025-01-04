class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        first = [-1] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            c_num = ord(c) - ord('a')

            if first[c_num] != -1:
                last[c_num] = i
            else:
                first[c_num] = i

        
        unique = 0
        for c_num in range(26):
            hashset = set()

            for i in range(first[c_num] + 1, last[c_num]):
                between = hashset.add(s[i])
            
            unique += len(hashset)

        return unique


