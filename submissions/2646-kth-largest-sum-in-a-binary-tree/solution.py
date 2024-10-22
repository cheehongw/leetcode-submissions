# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        # O(n)
        lvlSums = {}

        # O(n)
        def getLvlSum(node, lvl):
            if node == None:
                return

            lvlSums[lvl] = lvlSums.get(lvl, 0) + node.val

            if node.left:
                getLvlSum(node.left, lvl + 1)
            
            if node.right:
                getLvlSum(node.right, lvl + 1)
        
        getLvlSum(root, 0)
        
        sums = list(lvlSums.values())
        # print(sums)
        
        if len(sums) < k:
            return -1
        
        sums.sort()
        return sums[-k]
