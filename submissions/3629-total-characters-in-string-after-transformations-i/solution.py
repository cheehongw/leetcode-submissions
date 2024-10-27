class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        char_map = [0] * 26
        MOD = 10**9 + 7
        
        for c in s:
            char_map[ord(c) - ord('a')] += 1

        temp_map = [0]*26
        for i in range(t):
            for j in range(25):
                temp_map[j + 1] = char_map[j]

            temp_map[0] = char_map[25]
            temp_map[1] = (temp_map[1] + char_map[25]) % MOD

            for k in range(26):
                char_map[k] = temp_map[k]


        return sum(char_map) % MOD

        
            
        
        
