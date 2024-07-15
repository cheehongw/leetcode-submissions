# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        root_candidate = set()
        root_reject = set()

        for desc in descriptions:
            parent = nodes.get(desc[0], TreeNode(desc[0]))
            child = nodes.get(desc[1], TreeNode(desc[1]))
            isLeft = desc[2] == 1

            if (isLeft):
                parent.left = child
            else:
                parent.right = child

            nodes[desc[0]] = parent
            nodes[desc[1]] = child

            root_reject.add(desc[1])
            root_candidate.discard(desc[1])
            if (desc[0] not in root_reject):
                root_candidate.add(desc[0])
        
        
        return nodes[list(root_candidate)[0]]
