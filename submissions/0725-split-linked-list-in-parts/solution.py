# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # single pass would initialize k pointers and move them at varying speeds, but tedious to code out

        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        
        #divide the nodes into k parts
        parts_per_node = count // k
        remainder = count % k

        res = [None] * k

        ptr = ListNode(0, head)
        for i in range(k):

            res[i] = ptr.next if ptr else ptr
            if (ptr):
                ptr.next = None
            ptr = res[i]

            amount_to_advance = parts_per_node + 1 if i < remainder else parts_per_node

            for j in range(amount_to_advance - 1):
                ptr = ptr.next

        return res


        
