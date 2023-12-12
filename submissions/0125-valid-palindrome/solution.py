import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for i in range(ceil(len(cleanedStr)/2)):
            if cleanedStr[i] != cleanedStr[-(i + 1)]:
                return False

        return True

        
