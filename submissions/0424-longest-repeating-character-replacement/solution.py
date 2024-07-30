class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = [0] * 26
        l_ptr, r_ptr = 0, 0
        longest = 0
        max_f = 0

        while (r_ptr < len(s)):
            # incr r_ptr
            r_ptr += 1
            newChar = s[r_ptr - 1: r_ptr]
            freq_map[ord(newChar) - ord('A')] += 1
            max_f = max(max_f, freq_map[ord(newChar) - ord('A')])

            # check if window still valid
            # window valid if length of window - largest count in freq map <= k
            isValid = (r_ptr - l_ptr) - max_f <= k

            while not isValid:
                l_ptr += 1
                charRemoved = s[l_ptr - 1: l_ptr]
                freq_map[ord(charRemoved) - ord('A')] -= 1
                isValid = (r_ptr - l_ptr) - max_f <= k
        
            longest = max(longest, r_ptr - l_ptr)

        return longest 

    # def characterReplacement(self, s: str, k: int) -> int:
    #     freq_map = [0] * 26
    #     l_ptr, r_ptr = 0, 0
    #     longest = 0

    #     #O(26) time complexity
    #     def isValid():
    #         largest_count = 0

    #         # For loop runs in O(1) time since len(freq_map) == 26
    #         for count in freq_map:
    #             largest_count = max(largest_count, count)
            
    #         sum_all_counts = r_ptr - l_ptr
    #         isValid = (sum_all_counts - largest_count) <= k
    #         return isValid

    #     while (r_ptr < len(s)):
    #         # incr r_ptr
    #         r_ptr += 1
    #         newChar = s[r_ptr - 1: r_ptr]
    #         freq_map[ord(newChar) - ord('A')] += 1

    #         # check if window still valid
    #         # window valid if sum(all counts of freq_map) - largest count in freq map <= k
    #         while not isValid():
    #             l_ptr += 1
    #             charRemoved = s[l_ptr - 1: l_ptr]
    #             freq_map[ord(charRemoved) - ord('A')] -= 1
        
    #         longest = max(longest, r_ptr - l_ptr)

    #     return longest 
