# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ref_list = []

        while(head != None):
            ref_list.append(head)
            head = head.next

        l_ptr = 0
        r_ptr = len(ref_list) - 1
        l_turn = True
        while (l_ptr < r_ptr):
            if (l_turn):
                ref_list[l_ptr].next = ref_list[r_ptr]
                l_ptr += 1
            else:
                ref_list[r_ptr].next = ref_list[l_ptr]
                r_ptr -= 1

            l_turn = not l_turn

        ref_list[l_ptr].next = None

        return
