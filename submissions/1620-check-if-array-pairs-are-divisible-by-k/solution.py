class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # consider a number x, it is divisible by k if x % k == 0
        # if not divisible by k, then we want to find a  
        # second number y such that (y % k) + (x % k) == k
        # for each number in arr
        # x mod k == t --> requires a (k - t) to pair up with

        freq_map = {}

        for x in arr:
            remainder = x % k
            freq_map[remainder] = freq_map.get(remainder, 0) + 1

        for remainder, count in freq_map.items():
            other = k - remainder
            if remainder == 0:
                if count % 2 != 0:  
                    return False
            else:
                if freq_map.get(other, 0) != count:
                    return False
        

        return True

        
