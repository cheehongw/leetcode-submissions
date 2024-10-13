# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        sizes = []
        
        def isPBTree(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                node.val = 1
                sizes.append(1)
                return
            
            if node.left is None or node.right is None:
                node.val = 0
                isPBTree(node.left)
                isPBTree(node.right)
                return
                

            isPBTree(node.left)
            isPBTree(node.right)

            if(node.left.val != 0 and node.right.val != 0 and node.left.val == node.right.val):
                node.val = node.left.val + node.right.val + 1
                sizes.append(node.val)
            else:
                node.val = 0
        
        isPBTree(root)

        sizes.sort(reverse=True)

        if k > len(sizes):
            return -1
        
        else:
            return sizes[k-1]
