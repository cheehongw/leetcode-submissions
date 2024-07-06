class Solution:
    def isPalindrome(self, s: str) -> bool:
        remove_non_alnum = "".join([c for c in s if c.isalnum()])
        cleaned = remove_non_alnum.lower()

        i = 0
        j = len(cleaned) - 1
        while (i < j):
            if (cleaned[i] == cleaned[j]):
                i += 1
                j -= 1
            else: 
                return False

        return True
        
