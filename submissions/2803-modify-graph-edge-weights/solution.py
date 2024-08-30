class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        # obs: shortest path not including wildcard edges must == target
        # if shortest path not incl wildcard edges < target --> no solution
        # if shortest path not incl wildcard edges == target --> any soln
        # if shortest path not incl wildcard edges > target --> 
        #   can we get a shorter path incl wildcard edges? (how?, set all wildcard edges to 0) --> if yes --> soln found

        edges_not_incl_wildcards = []

        for e in edges:
            a, b, w = e[0], e[1], e[2]
            
            if (w != -1):
                edges_not_incl_wildcards.append(e)

        #djikstra 
        # 1. set up adj_xs
        # 2. initialize distance vector and previous node vector
        # 3. set up PQ with current best distance estimate to every node
        # 4. pop from PQ and update shortest paths
        def djikstra(n, edges, s, d):
            # 1. adj_xs
            adj_xs = [[] for _ in range(n)]
            for e in edges:
                a, b, w = e[0], e[1], e[2]
                adj_xs[a].append((b, w))
                adj_xs[b].append((a, w))
            
            # 2. distance vector D and prev node vector
            D = [sys.maxsize] * n
            D[s] = 0
            p = [-1] * n

            # 3. init pq with current best dist estimate
            pq = []
            for i in range(n):
                if (i == s):
                    pq.append((0, i))
                else:
                    pq.append((sys.maxsize, i))            
            heapify(pq)

            # pop from PQ and update shortest paths
            while pq:
                d, u = heappop(pq)
                if d == D[u]:
                    for neighbor, w in adj_xs[u]:
                        if (D[neighbor] > D[u] + w): #relaxable
                            D[neighbor] = D[u] + w
                            heappush(pq, (D[neighbor], neighbor))
                            p[neighbor] = u

            return D, p

        D, p = djikstra(n, edges_not_incl_wildcards, source, destination)

        if (D[destination] < target):
            return []
        

        matches_target = D[destination] == target

        for e in edges:
            if e[2] > 0:
                continue

            if (e[2] == -1):
                e[2] = target + 1 if matches_target else 1
                edges_not_incl_wildcards.append(e)

                if (not matches_target):
                    D, p = djikstra(n, edges_not_incl_wildcards, source, destination)

                    if D[destination] <= target:
                        matches_target = True
                        e[2] += target - D[destination]
            
        return edges if matches_target else []

        





        #     for e in edges:
        #         e[2] = sys.maxsize if e[2] == -1 else e[2]
            
        #     return edges
        # else:
        #     edges_not_incl_wildcards.extend(modified_wildcard_edges)
        #     D, p = djikstra(n, edges_not_incl_wildcards, source, destination)
        #     if (D[destination] <= target):
                
        #         used_wildcard_edges = set()
        #         curr_node = destination
                
        #         while (curr_node != source):
        #             temp = p[curr_node]
        #             a = min(temp, curr_node)
        #             b = max(temp, curr_node)
                    
        #             if (a, b) in wildcard_edges:
        #                 used_wildcard_edges.add((a,b))

        #             curr_node = temp

        #         is_first_edge_set = False
        #         for e in edges:
        #             u, v, w = e[0], e[1], e[2]
        #             if w == -1:
        #                 a = min(u, v)
        #                 b = max(u, v)

        #                 if (a, b) in used_wildcard_edges:
        #                     if (not is_first_edge_set):
        #                         final_w = 1 + (target - D[destination])
        #                         e[2] = final_w
        #                         is_first_edge_set = True
        #                     else:
        #                         e[2] = 1
        #                 else:
        #                     e[2] = 200000000 

        #         return edges

        #     else:
        #         return []




        



        
