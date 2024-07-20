class Solution:
    def minimumLength(self, s: str) -> int:
        char_map = {}
        char_map_2 = {}
        st = ['']*len(s)

        for i, c in enumerate(s):
            char_map[c] = char_map.get(c, 0) + 1
        
        for i, c in enumerate(s):
            char_map_2[c] = char_map_2.get(c, 0) + 1
            if (char_map[c] % 2 == 0):
                if char_map_2[c] == char_map[c] // 2 or char_map_2[c] == (char_map[c] // 2) + 1:
                    st[i] = c
            else:
                #odd
                if char_map_2[c] == (char_map[c] // 2) + 1:
                    st[i] = c

        return len(''.join(st))
                
                
