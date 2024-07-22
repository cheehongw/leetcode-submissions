class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h, n = zip(*sorted(zip(heights, names), reverse=True))
        return list(n)
