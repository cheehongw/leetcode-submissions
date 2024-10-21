class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        unique = set()
        
        def recurse(start_idx):

            if start_idx == len(s):
                return 0

            max_count = 0

            for end in range(start_idx + 1, len(s) + 1):
                substr = s[start_idx:end]
                if substr not in unique:
                    unique.add(substr)
                    max_count = max(recurse(end) + 1, max_count)
                    unique.remove(substr)

            return max_count
                

        return recurse(0)
