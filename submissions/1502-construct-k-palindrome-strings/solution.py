class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # count the freq of each char in s
        # chars with odd number must form their own unique palindrome string
        # chars with even number can be used to form 0/1:more palindrome strings

        freqs = [0]*26

        for c in s:
            freqs[ord(c) - ord('a')] += 1

        odd_freqs = 0
        even_counts = 0
        for x in freqs:
            if x % 2 == 1:
                odd_freqs += 1
                even_counts += (x - 1)
            else:
                even_counts += x        

        if k < odd_freqs:
            return False
        
        if k > odd_freqs + even_counts:
            return False
        
        return True





