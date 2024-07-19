# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newListHead = None
        newListTail = None

        if (list1 is None and list2 is None):
            return None
        elif (list1 is None):
            return list2
        elif (list2 is None):
            return list1
        else:
            if list1.val <= list2.val:
                newListHead = list1 
                newListTail = list1
                list1 = list1.next
            else:
                newListHead = list2
                newListTail = list2
                list2 = list2.next

        while (True):
            if (list1 is None and list2 is None):
                break

            if (list1 is None):
                newListTail.next = list2
                break
            
            if (list2 is None):
                newListTail.next = list1
                break

            if (list1.val <= list2.val):
                newListTail.next = list1
                newListTail = list1
                list1 = list1.next
            else:
                newListTail.next = list2
                newListTail = list2
                list2 = list2.next                

        return newListHead
