class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for i in arr1:
            while i != 0:
                prefixes.add(i)
                i = i // 10
        
        arr2.sort(reverse=True)
        
        max_prefix_len = 0 
        for i in arr2:
            len_i = len(str(i))
            if max_prefix_len >= len_i:
                break

            while len_i > max_prefix_len:
                if i in prefixes:
                    max_prefix_len = max(max_prefix_len, len(str(i)))
                    break
                else:
                    i = i // 10
                    len_i -= 1
        
        return max_prefix_len
            
            
            
