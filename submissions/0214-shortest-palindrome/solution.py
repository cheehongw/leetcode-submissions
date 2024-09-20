class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # idea: KMP lookup table to find shortest Palindrome
        # KMP lookup table property:
        # for any substring of string S, where the substring begins at S[0] but has 
        # length i <= len(s), we can find a place within S[0:i] 
        # such that a prefix of S matches a suffix of the substring
        

        def buildPrefixTable(s):
            prefix_table = [0]*len(s)
            length_of_longest_matching_prefix = 0

            for i, c in enumerate(s[1:]):
                if c == s[length_of_longest_matching_prefix]:
                    length_of_longest_matching_prefix += 1
                else:
                    while(length_of_longest_matching_prefix > 0 and c != s[length_of_longest_matching_prefix]):
                        # prefix_table[length_of_longest_matching_prefix - 1] is the character before c
                        # we just simply get the length of the longest prefix matching the character before c
                        # and hope we can continue w c
                        length_of_longest_matching_prefix = prefix_table[length_of_longest_matching_prefix - 1]

                    if c == s[length_of_longest_matching_prefix]:
                        length_of_longest_matching_prefix += 1

                prefix_table[i + 1] = length_of_longest_matching_prefix

            return prefix_table

        combined_str = s + '#' + s[::-1]
        prefix_table = buildPrefixTable(combined_str)
        
        longest_prefix = prefix_table[-1]
        remainder = s[longest_prefix:]

        return remainder[::-1] + s


