class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap1 = {}
        charMap2 = {}

        for c in s:
            charMap1[c] = charMap1.get(c, 0) + 1

        for c in t:
            charMap2[c] = charMap2.get(c, 0) + 1

        return charMap1 == charMap2
