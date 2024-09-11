class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xored = start ^ goal
        xored = f'{xored:b}'
        
        bitflips = 0
        for c in xored:
            if (c  == '1'):
                bitflips += 1

        return bitflips
