# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        parents = {root1.val : -1} if root1 else {}

        def recurse(node):
            
            if node is None:
                return
            
            if node.left:
                parents[node.left.val] = node.val
                recurse(node.left)
            
            if node.right:
                parents[node.right.val] = node.val
                recurse(node.right)
        
        recurse(root1)

        def recurse2(node):
            if node is None:
                return True

            if node.left:
                if parents.get(node.left.val, -2) != node.val:
                    return False
                
            if node.right:
                if parents.get(node.right.val, -2) != node.val:
                    return False
            
            parents.pop(node.val)
            return recurse2(node.right) and recurse2(node.left)

            
        
        if root1 and root2:
            return recurse2(root2) and root1.val == root2.val and len(parents) == 0
        elif root1 is None and root2 is None:
            return True
        else:
            return False
        


        
        
