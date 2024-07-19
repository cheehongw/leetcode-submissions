class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        col_max = [0]*len(matrix[0])
        row_min = [0]*len(matrix)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                row_min[row] = min(matrix[row])
                col_max[col] = max(col_max[col], matrix[row][col])
        
        lucky_num = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (col_max[col] == row_min[row]):
                    lucky_num.append(row_min[row])
        
        return lucky_num
