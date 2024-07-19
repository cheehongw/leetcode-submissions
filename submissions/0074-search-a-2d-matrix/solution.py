class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the correct row in O(log(m)) time
        
        s, l = 0, len(matrix)
        
        while(l - s > 1):
            pivot = (s + l) // 2
            first_elem = matrix[pivot][0]

            if (target < first_elem): 
                # target exists in rows s (incl) - l (excl)
                l = pivot
            else:
                s = pivot
        
        row = s
        #find the correct col in O(log(n)) time
        b, t = 0, len(matrix[0])

        while(t - b > 1):
            pivot = (t + b) // 2
            
            if (target < matrix[row][pivot]):
                t = pivot
            else:
                b = pivot
        
        return matrix[row][b] == target
