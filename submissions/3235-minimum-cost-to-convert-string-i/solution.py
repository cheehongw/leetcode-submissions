class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        MAX = pow(10, 7) 

        d = [[MAX] * 26 for i in range(26)]

        for i,c in enumerate(original):
            dest = changed[i]
            d[ord(c) - ord('a')][ord(dest) - ord('a')] = min(cost[i], d[ord(c) - ord('a')][ord(dest) - ord('a')])

        for i in range(26):
            d[i][i] = 0

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
        min_cost = 0
        for i in range(len(source)):
            source_char = source[i]
            dest_char = target[i]

            source_node = ord(source_char) - ord('a')
            dest_node = ord(dest_char) - ord('a')

            if (d[source_node][dest_node] >= MAX):
                print(source_node, dest_node, d[source_node][dest_node])
                return -1

            min_cost += d[source_node][dest_node]
            

        return min_cost





