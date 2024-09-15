class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = 0b0
        vowels_present_at_i = [0]

        for c in s:
            if c == 'a':
                bitmask = bitmask ^ 0b10000
            if c == 'e':
                bitmask = bitmask ^ 0b01000
            if c == 'i':
                bitmask = bitmask ^ 0b00100
            if c == 'o':
                bitmask = bitmask ^ 0b00010
            if c == 'u':
                bitmask = bitmask ^ 0b00001
            
            vowels_present_at_i.append(bitmask)
        
        start_pos = [-1] * 32

        # print(vowels_present_at_i)

        longest_ss = 0
        for i, x in enumerate(vowels_present_at_i):
            if start_pos[x] == -1:
                start_pos[x] = i
            
            longest_ss = max(longest_ss, i - start_pos[x])
        
        return longest_ss

