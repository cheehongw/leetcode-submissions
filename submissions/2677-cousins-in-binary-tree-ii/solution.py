# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = {}
        node_parent = {}
        node_val = {}

        # recursively visit every node and sums up the level
        # keeps track of each child's parent node
        # keeps track of each node's val
        def getLvlSum(node, lvl):
            if node == None:
                return
            
            levelSum[lvl] = levelSum.get(lvl, 0) + node.val
            node_val[node] = node.val

            if node.left:
                getLvlSum(node.left, lvl + 1)
                node_parent[node.left] = node

            if node.right:
                getLvlSum(node.right, lvl + 1)
                node_parent[node.right] = node

        
        getLvlSum(root, 0)

        def modifyNode(node, lvl):
            if node == None:
                return
            
            sibling_sum = 0

            if node_parent.get(node, None):
                sibling_sum += node_val[node_parent[node].left] if node_parent[node].left else 0
                sibling_sum += node_val[node_parent[node].right] if node_parent[node].right else 0
            else:
                sibling_sum = node_val[node]
            
            node.val = levelSum[lvl] - sibling_sum

            if node.left:
                modifyNode(node.left, lvl + 1)
            
            if node.right:
                modifyNode(node.right, lvl + 1)

        modifyNode(root, 0)

        return root

        
