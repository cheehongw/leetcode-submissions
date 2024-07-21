class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topoSort(edges):
            incoming_edges = [0]*k
            
            for edge in edges:
                a, b = edge[0], edge[1]
                incoming_edges[b - 1] += 1
            
            left_most = []
            
            for i in range(len(incoming_edges)):
                if incoming_edges[i] == 0:
                    left_most.append(i + 1)
            

            res = []
            # print(incoming_edges)
            # print(left_most)
            while left_most:
                node = left_most.pop()
                # print(node)
                res.append(node)

                for edge in edges:
                    a, b = edge[0], edge[1]
                    if (a == node):
                        incoming_edges[b - 1] -= 1
                        if (incoming_edges[b - 1] == 0):
                            left_most.append(b)
            
            return res

        
        rows_order = topoSort(colConditions)
        inverse_rows = {v : k for k, v in enumerate(rows_order)}
        cols_order = topoSort(rowConditions)
        inverse_cols = {v : k for k, v in enumerate(cols_order)}
        # print(inverse_rows)
        # print(inverse_cols)
        if (len(rows_order) < k or len(cols_order) < k):
            return []

        matrix = [[0]*k for i in range(k)]

        for i in range(1, k + 1):
            # print(inverse_cols.get(i, 0))
            # print(i)
            row = inverse_cols.get(i, 0)
            col = inverse_rows.get(i, 0)

            matrix[row][col] = i

        return matrix
        


        
