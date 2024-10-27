class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS,COLS=len(matrix),len(matrix[0])
        prev = [0]*(1+COLS)
        result = 0
        
        for i in range(ROWS):
            curr = [0]*(1+COLS)
            for j in range(1,1+COLS):
                if matrix[i][j-1]==1:
                    curr[j]=1+min(curr[j-1],prev[j-1],prev[j])
            result+=sum(curr)
            prev=curr
        return result 
