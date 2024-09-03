class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def convert(s) -> int:
            res = []
            for c in s:
                n = ord(c) - ord('a') + 1
                res.append(str(n))

            return int(''.join(res)) 


        def transform(i) -> int:
            
            transformed = 0

            while (i > 0):
                digit = i % 10
                i = i // 10
                transformed += digit
            return transformed

        x = convert(s)
        for i in range(k):
            x = transform(x)
        
        return x

        
