# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head

        while (ptr and ptr.next):
            GCD = gcd(ptr.val, ptr.next.val)
            new_node = ListNode(GCD, ptr.next)
            curr_node = ptr
            ptr = ptr.next
            curr_node.next = new_node
            
        return head
            
            

        # if head is None:
        #     return head

        # if head.next is None:
        #     return head

        # GCD = gcd(head.val, head.next.val)

        # next_node = head.next
        # new_node = ListNode(GCD, next_node)
        # head.next = new_node

        # self.insertGreatestCommonDivisors(next_node)

        # return head
        
