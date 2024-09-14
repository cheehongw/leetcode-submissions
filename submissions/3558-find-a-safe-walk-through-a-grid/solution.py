class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        LRTB = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque([(0,0), None])
        health_remaining = [[0] * COLS for _ in range(ROWS)]
        health_remaining[0][0] = health - grid[0][0]

        while queue:
            node = queue.popleft()

            if not node:
                if queue:
                    queue.append(None)
                
                continue
            
            x, y = node

            for dx, dy in LRTB:
                x_ = x + dx
                y_ = y + dy

                if (0 <= x_ < ROWS and 0 <= y_ < COLS):
                    new_health = health_remaining[x][y] - grid[x_][y_]
                    if new_health <= health_remaining[x_][y_]:
                        continue
                    
                    health_remaining[x_][y_] = new_health
                    queue.append((x_, y_))

            
        return health_remaining[ROWS - 1][COLS - 1] != 0
        
        # visited = set()
        # curr_health = health

        # def dfs(curr_node):
        #     nonlocal curr_health
        #     x, y = curr_node

        #     if grid[x][y] == 1:
        #         curr_health -= 1

        #     # print(f'{x}, {y} - {curr_health}')
            
        #     if curr_health <= 0:
        #         if grid[x][y] == 1:
        #             curr_health += 1
        #         return False

        #     if curr_node == (ROWS - 1, COLS - 1):
        #         return True

        #     visited.add(curr_node)           

        #     res = False
        #     for dx, dy in LRTB:
        #         x_ = x + dx
        #         y_ = y + dy

        #         if (0 <= x_ < ROWS and 0 <= y_ < COLS and (x_, y_) not in visited):
        #             res = res or dfs((x_, y_))
        #             if res:
        #                 break
            
        #     if grid[x][y] == 1:
        #         curr_health += 1

        #     visited.remove(curr_node)
        #     return res

        # return dfs((0,0))

                

            


        
