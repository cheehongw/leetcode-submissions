class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        isDistinct = set()
        nonDistinct = set()

        for s in arr:
            if (s not in isDistinct and s not in nonDistinct):
                isDistinct.add(s)
            elif(s in isDistinct):
                isDistinct.remove(s)
                nonDistinct.add(s)

        for s in arr:
            if s in isDistinct:
                k -= 1
                if (k == 0):
                    return s
            
        return ""
        
