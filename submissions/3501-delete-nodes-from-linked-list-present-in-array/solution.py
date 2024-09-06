# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:


        def recursiveModifiedList(nums, head):
            if head == None:
                return None

            if head.val in nums:
                return recursiveModifiedList(nums, head.next)
            else:
                head.next = recursiveModifiedList(nums, head.next)
                return head
        
        return recursiveModifiedList(set(nums), head)
