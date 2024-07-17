# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDeleteSet = set(to_delete)
        roots = {}
        roots[root.val] = root

        if (len(toDeleteSet) == 0):
            return roots.values()
        else:
            self.delNodesHelper(root, toDeleteSet, roots)


        return roots.values()

        
    def delNodesHelper(self, root, to_delete, roots):
        if(len(to_delete) == 0):
            return
    
        if(root is None):
            return

        if (root.val in to_delete):
            to_delete.discard(root.val)
            roots.pop(root.val, None)
            
            if (root.left is not None):
                roots[root.left.val] = root.left
            
            if (root.right is not None):
                roots[root.right.val] = root.right

        left = root.left
        right = root.right
        if (root.left is not None and root.left.val in to_delete):
            root.left = None
        if (root.right is not None and root.right.val in to_delete):
            root.right = None

        self.delNodesHelper(left, to_delete, roots)
        self.delNodesHelper(right, to_delete, roots)
