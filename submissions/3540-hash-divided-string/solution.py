class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        x = k
        hash_val = 0

        res = []

        for c in s:
            x -= 1
            hash_val += ord(c) - ord('a')
            
            if (x == 0):
                x = k
                res.append(chr(ord('a') + hash_val % 26))
                hash_val = 0
        
        return ''.join(res)
            

            
