class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # initiate window from first char of s
        # expand window until it contains t
        # reduce window from the left side until it stops containing t
        # repeat from step 2
        
        freq_map = {}
        for c in t:
            freq_map[c] = freq_map.get(c, 0) + 1

        unique_chars = len(freq_map.keys())

        l_ptr, r_ptr = 0,0
        has_t = False

        def contains_t(char, isNewChar):
            nonlocal unique_chars

            if isNewChar:
                if char in freq_map:
                    freq_map[char] -= 1
                    if freq_map[char] == 0:
                        unique_chars -= 1
            else:
                if char in freq_map:
                    freq_map[char] += 1
                    if freq_map[char] > 0:
                        unique_chars += 1
            
            return unique_chars == 0


        min_substr = ""
        shortest_viable_window_size = 10**5 + 1

        while (not has_t and r_ptr < len(s)) or (has_t and l_ptr < r_ptr):
            if not has_t:
                r_ptr += 1
                new_char = s[r_ptr - 1]
                has_t = contains_t(new_char, True)
            else:
                l_ptr += 1
                removed_char = s[l_ptr - 1]
                has_t = contains_t(removed_char, False)

            if (has_t and (r_ptr - l_ptr) < shortest_viable_window_size):
                shortest_viable_window_size = r_ptr - l_ptr
                min_substr = s[l_ptr: r_ptr]
        
        return min_substr






            
        
