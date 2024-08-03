class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        N_ROWS = len(grid)
        N_COLS = len(grid[0])

        min_flips = 0
        for r in range(N_ROWS // 2):
            for c in range(N_COLS // 2):
                top_left = grid[r][c]
                top_right = grid[r][N_COLS - 1 - c]
                bot_left = grid[N_ROWS - 1 - r][c]
                bot_right = grid[N_ROWS - 1 - r][N_COLS - 1 - c]

                sum = top_left + top_right + bot_left + bot_right
                
                flips = 0
                if (sum == 2):
                    flips = 2
                elif (sum == 3 or sum == 1):
                    flips = 1
                
                min_flips += flips

        flips = 0
        ones = 0

        if (N_ROWS % 2 == 1):
            odd_row = grid[N_ROWS // 2]
            l_ptr, r_ptr = 0, len(odd_row) - 1
            while (l_ptr < r_ptr):
                first = odd_row[l_ptr]
                last = odd_row[r_ptr]
                l_ptr += 1
                r_ptr -= 1
                
                if (first != last):
                    flips += 1
                else:
                    if (first == 1):
                        ones += 2
                
        if (N_COLS % 2 == 1):
            col_idx = N_COLS // 2
            l_ptr, r_ptr = 0, len(grid) - 1
            while (l_ptr < r_ptr):
                first = grid[l_ptr][col_idx]
                last = grid[r_ptr][col_idx]
                l_ptr += 1
                r_ptr -= 1

                if (first != last):
                    flips += 1
                else:
                    if (first == 1):
                        ones += 2
        
        central_flip = 0
        if (N_COLS % 2 == 1 and N_ROWS % 2 == 1):
            val = grid[N_ROWS // 2][N_COLS // 2]
            if val == 1:
                central_flip += 1

        if ones % 4 == 0:
            return min_flips + flips + central_flip
        elif ones % 4 == 2:
            if (flips >= 1):
                return min_flips + flips + central_flip
            else:
                return min_flips + 2 + central_flip


            
        
