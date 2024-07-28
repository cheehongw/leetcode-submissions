class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # do a bfs starting from 1 to n
        # shortest time will be correlated to the shortest path
        # find the shortest path from one edge to the other
        
        visited = {}
        visited_2 = {}
        
        adj_xs = {}

        for edge in edges:
            v1, v2 = edge[0], edge[1]
            xs_1 = adj_xs.get(v1, set())
            xs_1.add(v2)
            adj_xs[v1] = xs_1
            xs_2 = adj_xs.get(v2, set())
            xs_2.add(v1)
            adj_xs[v2] = xs_2

        nodes = deque([1, None])
        dist = 0
        shortest_path = set()

        while(True):
            # print(nodes, dist, shortest_path)
            node = nodes.popleft()

            if node == n:
                shortest_path.add(dist)
                if (len(shortest_path) == 2):
                    break

            if (node in visited and node is not None):
                if (node in visited_2 and node is not None):
                    continue
                
                if visited[node] < dist:
                    visited_2[node] = dist
                else:
                    continue
            
            visited[node] = visited.get(node, dist)
            if (node is None):
                #end of bfs wave
                dist += 1
                if (len(nodes) == 0):
                    break
                nodes.append(None)
                
            else:

                neighbours = adj_xs[node]
                for neighbour in neighbours:
                    nodes.append(neighbour)


        def compute_time(n_edges):
            time_elapsed = 0
            time_to_signal_green = 0
            signal_green = True
            while n_edges:
                print(time_elapsed)
                if (signal_green):
                    time_elapsed += time
                else:
                    time_elapsed += time_to_signal_green
                    time_elapsed += time
                    signal_green = True

                if ((time_elapsed // change) % 2 == 1):
                    signal_green = False
                    time_to_signal_green = change - (time_elapsed % change)

                n_edges -= 1

            return time_elapsed


                
        
        print(shortest_path)
        
        if len(shortest_path) == 1:
            shortest_path.add(list(shortest_path)[0] + 2)
        
        timings = [compute_time(e) for e in shortest_path]
        return max(timings)
