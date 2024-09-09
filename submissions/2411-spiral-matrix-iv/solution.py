# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        RDLU = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        matrix = [[-1]*n for _ in range(m)]

        ptr = head
        x, y = 0, 0
        while ptr:
            matrix[x][y] = ptr.val
            ptr = ptr.next

            dx, dy = RDLU[direction]
            _x = x + dx
            _y = y + dy

            if (not (0 <= _x < m and 0 <= _y < n) or matrix[_x][_y] != -1):
                direction = (direction + 1) % 4
                dx, dy = RDLU[direction]
            
            x += dx
            y += dy
        
        return matrix
                

