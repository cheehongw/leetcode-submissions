class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
        row_flips = 0
        for row in grid:
            l_ptr, r_ptr = 0, len(row) - 1
            while(l_ptr <= r_ptr):
                first = row[l_ptr]
                last = row[r_ptr]

                if (first != last):
                    row_flips += 1
                l_ptr += 1
                r_ptr -= 1
        

        col_flips = 0
        for col_idx in range(len(grid[0])):
            l_ptr, r_ptr = 0, len(grid) - 1
            while(l_ptr <= r_ptr):
                first = grid[l_ptr][col_idx]
                last = grid[r_ptr][col_idx]

                if (first != last):
                    col_flips += 1

                l_ptr += 1
                r_ptr -= 1
        
        return min(col_flips, row_flips)




        
