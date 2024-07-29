"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        ptr = head

        while ptr is not None:
            ptr.next = Node(ptr.val, ptr.next, ptr.random)
            ptr = ptr.next.next
        

        ptr = head
        while ptr is not None:
            ptr.next.random = ptr.next.random.next if ptr.next.random is not None else None
            ptr = ptr.next.next
        
        
        ptr = head
        new_head = head.next if head is not None else head

        while ptr is not None:
            copied = ptr.next
            ptr.next = copied.next
            copied.next = copied.next.next if copied.next is not None else None
            ptr = ptr.next
        
        return new_head
            
        
