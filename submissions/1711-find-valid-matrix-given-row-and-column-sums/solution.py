class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N_ROWS = len(rowSum)
        N_COLS = len(colSum)

        # we will return this matrix
        matrix = [[0] * N_COLS for i in range(N_ROWS)]

        for i in range(N_ROWS):
            matrix[i][0] = rowSum[i]
        
        #proceed to "smear" the values in each row across the columns
        for i in range(N_COLS):
            expected_colSum = colSum[i]
            for j in range(N_ROWS):
                val = matrix[j][i]
                matrix[j][i] = min(expected_colSum, val)
                carry = val - expected_colSum if val - expected_colSum > 0 else 0
                #update the expected_colSum
                expected_colSum -= matrix[j][i]
                ## update the carry
                if (carry != 0):
                    matrix[j][i+1] = carry

        return matrix

                





            

            
            
