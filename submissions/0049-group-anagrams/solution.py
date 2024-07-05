from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # define hash function that hashes all strings with same chars together
        # easiest: arrange a count of a-z, then concat them together

        groups = defaultdict(list)

        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            xs = groups[tuple(arr)]
            xs.append(s)
            groups[tuple(arr)] = xs
        
        return groups.values()

        

                



        
