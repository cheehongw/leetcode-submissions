"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []

        post_child = []
        if root.children:
            for child in root.children:
                post_child.extend(self.postorder(child))

        post_child.append(root.val)

        return post_child    
        
        



