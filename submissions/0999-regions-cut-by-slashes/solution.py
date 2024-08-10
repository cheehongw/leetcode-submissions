class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        mat = [[0]*3*n for i in range(3*n)]

        def updateMatrix(i, j, letter):
            i = i*3
            j = j*3

            if letter == ' ':
                return
            
            if letter == '/':
                mat[i][j + 2] = 1
                mat[i + 1][j + 1] = 1
                mat[i + 2][j] = 1
                return

            if letter == '\\':
                mat[i][j] = 1
                mat[i + 1][j + 1] = 1
                mat[i + 2][j + 2] = 1
                return    


        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                updateMatrix(i, j, c)

        def dfs(i, j):
            if(mat[i][j] == 1):
                return
            
            mat[i][j] = 1
            
            LRTB = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            
            for x, y in LRTB:
                i_ = i + x
                j_ = j + y

                if ( 0 <= i_ < len(mat) and 0 <= j_ < len(mat[0])):
                    dfs(i_, j_)

            return


        components = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dfs(i, j)
                    components += 1

        
        return components

        




                
        
