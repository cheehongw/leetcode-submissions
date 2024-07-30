# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # O(n) time complexity
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
    #     def addTwoNumbersWithCarry(l1, l2, carry):
            
    #         l1_val = 0 if l1 is None else l1.val
    #         l2_val = 0 if l2 is None else l2.val

    #         sum = l1_val + l2_val + carry
    #         if (l1 is None and l2 is None and carry == 0):
    #             return None

    #         val = sum % 10
    #         carry = 1 if sum >= 10 else 0
    #         return ListNode(val, addTwoNumbersWithCarry(l1.next if l1 else None, l2.next if l2 else None, carry))

    #     return addTwoNumbersWithCarry(l1, l2, 0)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        headNode = None
        ptr = None
        while (l1 or l2 or carry):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum = l1_val + l2_val + carry
            computedVal = sum % 10
            carry = sum // 10
            
            if headNode:
                ptr.next = ListNode(computedVal, None)
                ptr = ptr.next
            else:
                headNode = ListNode(computedVal, None)
                ptr = headNode
            
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        
        return headNode


