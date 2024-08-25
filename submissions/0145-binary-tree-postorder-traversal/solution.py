# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []

        post_left = self.postorderTraversal(root.left)
        post_right = self.postorderTraversal(root.right)

        post_left.extend(post_right)
        post_left.append(root.val)

        return post_left
        
