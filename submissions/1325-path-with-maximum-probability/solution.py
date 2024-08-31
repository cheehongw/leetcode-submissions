class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj_xs = [[] for _ in range(n)]

        for i, e in enumerate(edges):
            a, b = e[0], e[1]
            
            if (succProb[i] == 0):
                continue
            weight = -log(succProb[i])

            adj_xs[a].append((b, weight))
            adj_xs[b].append((a, weight))
        
        pq = []
        D = [sys.maxsize]*n
        D[start_node] = 0

        for i in range(0, n):
            if (i == start_node):
                pq.append((0, i))
            else:
                pq.append((sys.maxsize, i))

        heapify(pq)

        while (pq):
            d, u = heappop(pq)
            if (d == D[u]):
                for v, w in adj_xs[u]:
                    if (D[v] > D[u] + w):
                        D[v] = min(D[v], D[u] + w)
                        heappush(pq, (D[v], v))

        if D[end_node] == sys.maxsize:
            return 0
        else:
            return exp(-D[end_node])

