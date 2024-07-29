# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
# O(n) - time complexity
# O(n) - space complexity
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
