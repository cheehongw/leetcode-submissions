class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_tree = [-1] * n

        def valid_par(node, char):

            par = parent[node]
            if par == -1:
                return -1
                
            if s[par] != char:
                return valid_par(par, char)
            else:
                return par


        for i in range(n):
            new_par = valid_par(i, s[i])
            new_tree[i] = new_par if new_par != -1 else parent[i]


        ans = [1] * n
        
        for node in range(n):
            par = new_tree[node]
            
            while par != -1:
                ans[par] += 1
                par = new_tree[par]


        return ans
            
