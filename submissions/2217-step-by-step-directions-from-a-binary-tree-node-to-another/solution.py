# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        results_to_start = []
        results_to_end = []
        self.findValue(root, startValue, results_to_start)
        self.findValue(root, destValue, results_to_end)

        path_to_start, nodes_to_start = zip(*results_to_start)
        path_to_end, nodes_to_end = zip(*results_to_end)
        
        common_ancestor = 0
        for i in range(min(len(nodes_to_start), len(nodes_to_end))):

            to_start = nodes_to_start[i]
            to_end = nodes_to_end[i]
            
            if (to_start == to_end):
                common_ancestor = i
            else:
                break

        
        dist_lca_start = len(nodes_to_start) - 1 - common_ancestor
        path_to_lca_from_start = 'U' * dist_lca_start

        path_from_lca_to_end = ''.join(path_to_end[common_ancestor:])

        return path_to_lca_from_start + path_from_lca_to_end

    def findValue(self, root, value, path) -> List[str]:
        if (root == None):
            return None
        
        if (root.val == value):
            path.append(('', root.val))
            return True

        path.append(('L', root.val))
        tryLeft = self.findValue(root.left, value, path)
        if (not tryLeft):
            path.pop()
        else:
            return True
        
        path.append(('R', root.val))
        tryRight = self.findValue(root.right, value, path)
        if (not tryRight):
            path.pop()
        else:
            return True
        
        return False

        
        
