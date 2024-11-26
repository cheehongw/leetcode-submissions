class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        potential_champions = set(range(n))
        
        for e in edges:
            u, v = e[0], e[1]
            if v in potential_champions:
                potential_champions.remove(v)

        if len(potential_champions) == 1:
            return potential_champions.pop()
        else:
            return -1

        
