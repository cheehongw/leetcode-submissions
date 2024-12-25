# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if root is None:
            return res

        queue = deque([root, None])

        level_max = None
        while queue:
            node = queue.popleft()
            if node:
                level_max = max(level_max, node.val) if level_max is not None else node.val

                if node and node.left:
                    queue.append(node.left)
                
                if node and node.right:
                    queue.append(node.right)
            else:
                res.append(level_max)
                level_max = None
                if queue:
                    queue.append(None)
        
        return res

            



    
    
