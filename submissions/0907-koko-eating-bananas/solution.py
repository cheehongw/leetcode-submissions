class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min hours required = len(piles)
        # max hours allowed = h
        # max eating eating speed k = max(piles) //so she can consume all piles each hour to achieve the fastest time
        # min eating speed lower bound = 1 given that koko must eat

        # binary search to find the min eating speed such that it is valid
        # determining whether a eating speed is valid:
        #     compute the hrs per pile for n piles - O(n)

        #binary search = O(logn)
        #Overall time complexity - O(nlogn)

        def canKokoFinish(eatingSpeed):
            
            hours_needed = 0
            for pile in piles:
                hours = ceil(pile / eatingSpeed)
                hours_needed += hours
                
                if hours_needed > h:
                    return False
            
            return True
        
        lower = 1
        upper = max(piles)
        pivot = (lower + upper) // 2

        while (upper - lower > 0):
            canFinish = canKokoFinish(pivot)
            if (canFinish):
                # if koko can finish - pivot is a valid, smaller, upperBound
                upper = pivot
            else:
                #  if koko cannot finish - pivot is an invalid, larger lower Bound
                #  therefore, we try pivot + 1 as the possible lower bound
                lower = pivot + 1

            pivot = (lower + upper) // 2

        return lower

