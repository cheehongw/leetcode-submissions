# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def height(root):
            if root is None:
                return (0, True)
            else:
                l_h, l_balanced = height(root.left)
                r_h, r_balanced = height(root.right)

                balanced = abs(l_h - r_h) <= 1 and l_balanced and r_balanced

                return max(r_h, l_h) + 1, balanced
        
        h, b = height(root)

        return b
