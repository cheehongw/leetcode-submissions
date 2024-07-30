# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def heightofTree(root, max_diameter):
            if root is None:
                return 0, max(0, max_diameter)
            
            if root.left is None and root.right is None:
                return 0, max(0, max_diameter)
            
            l_height, max_diameter = heightofTree(root.left, max_diameter)
            r_height, max_diameter = heightofTree(root.right, max_diameter)

            diameter_of_left_subtree = 0 if root.left is None else 1 + l_height
            diameter_of_right_subtree = 0 if root.right is None else 1 + r_height
            diameter =  diameter_of_left_subtree + diameter_of_right_subtree
            
            max_diameter = max(diameter, max_diameter) 

            height = 1 + max(l_height, r_height)

            return height, max_diameter

        h, d = heightofTree(root, 0)
        return d
            
