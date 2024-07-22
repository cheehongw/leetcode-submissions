# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr_1 = head
        ptr_2 = head
        before = None

        while(n > 0):
            ptr_1 = ptr_1.next
            n -= 1

        while(ptr_1 is not None):
            ptr_1 = ptr_1.next
            before = ptr_2
            ptr_2 = ptr_2.next

        if (before is None):
            return ptr_2.next

        before.next = ptr_2.next
        ptr_2.next = None

        return head
        
        
