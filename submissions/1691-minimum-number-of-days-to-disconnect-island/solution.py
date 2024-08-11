class Solution:

    def minDays(self, grid: List[List[int]]) -> int:
        N_ROWS, N_COLS = len(grid), len(grid[0])

        def count_islands():
            visited = [[-1] * N_COLS for _ in range(N_ROWS)]
            count = 0
            for i in range(N_ROWS):
                for j in range(N_COLS):
                    if (grid[i][j] == 1 and visited[i][j] == -1):
                        dfs(i, j, visited)
                        count += 1

            return count

        
        def dfs(row, col, visited):
            LRTB = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            if visited[row][col] != -1:
                return
            
            visited[row][col] = 1
            
            for x,y in LRTB:
                row_ = row + x
                col_ = col + y

                if (0 <= row_ < N_ROWS and 0 <= col_ < N_COLS and grid[row_][col_] == 1):
                    dfs(row_, col_, visited)

        island_count = count_islands()

        if island_count == 0 or island_count > 1:
            return 0
        
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if (grid[i][j] == 1):
                    grid[i][j] = 0
                    c = count_islands()
                    if c == 0 or c > 1:
                        return 1
                    grid[i][j] = 1
        
        return 2
            

            




            

        
                
