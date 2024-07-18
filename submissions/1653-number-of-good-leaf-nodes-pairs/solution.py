# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        parents = {}
        leaves = []

        def find_parents_and_leaves(node):

            if (node.left is not None):
                parents[node.left] = node
                find_parents_and_leaves(node.left)

            if (node.right is not None):    
                parents[node.right] = node
                find_parents_and_leaves(node.right)
        
            if (node.left is None and node.right is None):
                leaves.append(node)
        
        find_parents_and_leaves(root)
        
        good_pairs = 0
        def dfs(node, prev_node, n):
            nonlocal good_pairs
            
            if (n < 0):
                return

            if (node.left is None and node.right is None):
                good_pairs += 1
            
            parent = parents.get(node, None) 
            left_child = node.left 
            right_child = node.right 

            possible_nodes = [parent, left_child, right_child]
            possible_nodes = [x if x != prev_node else None for x in possible_nodes ]            

            for x in possible_nodes:
                if (x):
                    dfs(x, node, n - 1)
        
        for leaf in leaves:
            dfs(leaf, None, distance)


        return (good_pairs - len(leaves))// 2
            

