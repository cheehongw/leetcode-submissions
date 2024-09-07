# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(head, root):
            if root is None and head is not None:
                return False
            
            if head is None:
                return True

            if head.val == root.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)
            else:
                return False


        if root is None:
            return False
        elif (head.val != root.val):
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        else:
            return dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)



        
