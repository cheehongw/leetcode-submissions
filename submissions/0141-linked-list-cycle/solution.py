# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head == None):
            return False
        
        f_p = head
        s_p = {'stored': head.val, 'node': head}

        def advance_fp():
            nonlocal f_p
            if f_p.next == None:
                return 0
            
            f_p = f_p.next
            if f_p.val == None:
                return 1

            return 2

        def advance_sp():
            nonlocal s_p
            s_p['node'].val = s_p['stored']
            s_p['node'] = s_p['node'].next
            s_p['stored'] = s_p['node'].val
            s_p['node'].val = None



        while True:
            res = advance_fp()
            if (res == 1):
                return True
            if (res == 0):
                return False
            
            advance_sp()
            
            res = advance_fp()
            if (res == 1):
                return True
            if (res == 0):
                return False
