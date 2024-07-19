# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # somehow do head.next.next = head
        # head.next.next.next = head.next and so forth

        def helper(prev, curr):
            
            if (curr == None):
                return prev

            next = curr.next
            curr.next = prev

            return helper(curr, next)

        return helper(None, head)
