class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charmap = {}
        for char in s:
            if char not in charmap:
                charmap[char] = 1
            else:
                charmap[char] += 1
        
        for char in t:
            if char not in charmap:
                return False
            else:
                charmap[char] -= 1
                if charmap[char] < 0:
                    return False
        
        return True
            
        
