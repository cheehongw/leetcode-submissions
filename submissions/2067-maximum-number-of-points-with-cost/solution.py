class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        previous_row = points[0]

        for row in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            current_row = [0] * cols

            # Calculate left-to-right maximum
            left_max[0] = previous_row[0]
            for col in range(1, cols):
                left_max[col] = max(left_max[col - 1] - 1, previous_row[col])

            # Calculate right-to-left maximum
            right_max[-1] = previous_row[-1]
            for col in range(cols - 2, -1, -1):
                right_max[col] = max(right_max[col + 1] - 1, previous_row[col])

            # Calculate the current row's maximum points
            for col in range(cols):
                current_row[col] = points[row][col] + max(
                    left_max[col], right_max[col]
                )

            # Update previous_row for the next iteration
            previous_row = current_row

        # Find the maximum value in the last processed row
        return max(previous_row)



    # def maxPoints(self, points: List[List[int]]) -> int:
    #     N_ROWS = len(points)
    #     N_COLS = len(points[0])

    #     memo = [[None for _ in range(N_COLS)] for _ in range(N_ROWS) ]

    #     def dpMaxPoints(row, prevCol):

    #         if row >= N_ROWS:
    #             return 0

    #         if memo[row][prevCol] is not None:
    #             return memo[row][prevCol]
            
    #         p = -99999999
    #         for i, col in enumerate(points[row]):
                
    #             _l = i - 1 if i - 1 >= 0 else 0
    #             _r = i + 1 if i + 1 < N_COLS else N_COLS - 1

    #             if points[row][_l] - col > 1 or points[row][_r] - col > 1:
    #                 continue

    #             p = max(dpMaxPoints(row + 1, i) + col - abs(prevCol - i), p)
            
    #         memo[row][prevCol] = p
    #         return p


    #     p = -99999999

    #     for i, col in enumerate(points[0]):
    #         _l = i - 1 if i - 1 >= 0 else 0
    #         _r = i + 1 if i + 1 < N_COLS else N_COLS - 1
    #         if points[0][_l] - col > 1 or points[0][_r] - col > 1:
    #             continue
    #         p = max(dpMaxPoints(1, i) + col, p) 
        
    #     return p
