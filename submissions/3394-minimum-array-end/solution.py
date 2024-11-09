class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        # smallest number is x itself - 
        # next largest number -> flip a 0 to 1

        # count bits in x
        def merge(merge_with):
            res = x
            mask = 1
            while merge_with:
                if (res & mask) == 0:
                    res = res | ((merge_with & 1) * mask)
                    merge_with = merge_with >> 1
                
                mask <<= 1
            
            return res

        return merge(n - 1)
        
            
