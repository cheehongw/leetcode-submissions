class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        for i in range(n - 1):
            inverted = s.replace('0', '2').replace('1', '0').replace('2', '1')
            reverse = inverted[::-1]

            s = s + '1' + reverse

        return s[k - 1]
        
