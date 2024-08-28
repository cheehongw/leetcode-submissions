class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        LRTB = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        island_id = 2

        def dfs(i, j, id):
            grid1[i][j] = id
            for x, y in LRTB:
                _x = i + x
                _y = j + y

                if (0 <= _x < m and 0 <= _y < n and grid1[_x][_y] == 1):
                    dfs(_x, _y, id)

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    dfs(i, j, island_id)
                    island_id += 1


        def dfs_2(i, j, id):
            grid2[i][j] = 0

            res = grid1[i][j] == id and id != 0

            for x, y in LRTB:
                _x = i + x
                _y = j + y

                if (0 <= _x < m and 0 <= _y < n and grid2[_x][_y] == 1):
                    res = dfs_2(_x, _y, id) and res

            return res

        sub_island_count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res = dfs_2(i, j, grid1[i][j])

                    if (res):
                        sub_island_count += 1

        return sub_island_count

        



                

        
