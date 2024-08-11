class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        adj_xs = {}
        
        for e in edges:
            u, v = e[0], e[1]
            adj_xs[u] = adj_xs.get(u, set())
            adj_xs[u].add(v)

            adj_xs[v] = adj_xs.get(v, set())
            adj_xs[v].add(u)
            

        desc_xs = {}
        visited = set()
        toVisit = deque([0])
        while toVisit:
            node = toVisit.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neighbor in adj_xs[node]:
                if (neighbor not in visited):
                    desc_xs[node] = desc_xs.get(node, set())
                    desc_xs[node].add(neighbor)
                    toVisit.append(neighbor)

        # print(desc_xs)

        def countNodesAndGood(node):
            if not desc_xs.get(node, []):
                return 1, 1
            
            res = []
            for child in desc_xs.get(node):
                res.append(countNodesAndGood(child))

            # print(res)

            counts, good_num = zip(*res)

            good = True
            for c in counts:
                good = good and c == counts[0]
            
            final_good = (1 if good else 0) + sum(good_num)

            return sum(counts) + 1, final_good

        return countNodesAndGood(0)[1]
