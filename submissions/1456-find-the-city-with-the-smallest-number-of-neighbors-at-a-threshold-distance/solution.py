class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = [[99999999] * n for i in range(n)]

        for e in edges:
            to, fr, weight = e[0], e[1], e[2]

            mat[to][fr] = weight
            mat[fr][to] = weight

        for i in range(n):
            mat[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j],  mat[i][k] + mat[k][j])
        
        counts = [0]*n

        for i in range(n):
            city = mat[i]
            for idx, d in enumerate(city):
                if (d <= distanceThreshold and idx != i):
                    counts[i] += 1

        max_city = 0
        min_count = n
        
        for i in range(n):
            if (counts[i] <= min_count):
                min_count = counts[i]
                max_city = i

        return max_city


