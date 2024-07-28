class Solution:
    
    # time complexity - O(n)
    # space complexity - O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr_chars = set()
        curr_longest = 0
        l_ptr, r_ptr = 0, 0

        # window will be from s[l_ptr:r_ptr]

        while r_ptr != len(s):
            r_ptr += 1
            
            #todo: max r_ptr == n
            new_char = s[r_ptr - 1: r_ptr]

            if new_char in curr_chars:
                while(new_char in curr_chars):
                    l_ptr += 1
                    char_removed = s[l_ptr - 1: l_ptr]
                    curr_chars.remove(char_removed)
                
            curr_chars.add(new_char)
            length = r_ptr - l_ptr
            curr_longest = max(length, curr_longest)

        return curr_longest
            # if new_char not in curr_chars:
            #     curr_chars.add(new_char)
            #     length = r_ptr - l_ptr
            #     curr_longest = max(length, curr_longest)
    
            # else:
            #     #encountered repeated character
            #     while(new_char in curr_chars):
            #         l_ptr += 1
            #         char_removed = s[l_ptr - 1: l_ptr]
            #         curr_chars.remove(char_removed)
                
            #     curr_chars.add(new_char)
            #     length = r_ptr - l_ptr
            #     curr_longest = max(length, curr_longest)







        
