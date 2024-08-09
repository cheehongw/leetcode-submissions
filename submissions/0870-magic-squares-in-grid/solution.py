class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        N_ROWS = len(grid)
        N_COLS = len(grid[0])


        def isMagicSquare(topLeft):
            row, col = topLeft
            rows = [0, 0, 0]
            cols = [0, 0, 0]
            diags = [0, 0]
            isSeen = set()

            for i in range(3):
                for j in range(3):
                    row_ = row + i
                    col_ = col + j
                    if (0 <= row_ < N_ROWS and 0 <= col_ < N_COLS):
                        val = grid[row_][col_]
                        if val in isSeen:
                            return False

                        if not (1 <= val <= 9):
                            return False
                        
                        isSeen.add(val)

                        rows[i] += val
                        cols[j] += val

                        if (i == j):
                            diags[0] += val
                            if (diags[0] > 15):
                                return False
                        
                        if ((i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0)):
                            diags[1] += val
                            if (diags[0] > 15):
                                return False

                        if (rows[i] > 15 or cols[j] > 15):
                            return False
                    else:
                        return False

            for i in rows:
                if i != 15:
                    return False
            
            for i in cols:
                if i != 15:
                    return False
            
            for k in diags:
                if k != 15:
                    return False

            return True

        count = 0

        for i in range(N_ROWS):
            for j in range(N_COLS):
                res = isMagicSquare((i, j))
                if res:
                    count += 1
        
        return count
