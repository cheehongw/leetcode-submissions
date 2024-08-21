# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if (subRoot is None):
            return True
        
        if (root is None):
            return False


        if (root.val == subRoot.val):
            return \
            (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)) \
            or self.isSubtree(root.left, subRoot) \
            or self.isSubtree(root.right, subRoot)
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, other):
        
        if (root is None and other is None):
            return True
        
        if (root is None or other is None):
            return False

        return root.val == other.val \
        and self.isSameTree(root.left, other.left) \
        and self.isSameTree(root.right, other.right)


