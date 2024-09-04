class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dir = 0     # up - 0, right - 1, down - 2, left - 3
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles_set = set()

        for o in obstacles:
            a, b = o[0], o[1]
            obstacles_set.add((a, b))

        max_dist = 0

        for c in commands:
            if c == -1:
                dir = (dir + 1) % 4
            elif c == -2:
                dir = (dir - 1) % 4
            else:
                while (c > 0):
                    dx, dy = DIR[dir]
                    temp_x = x + dx
                    temp_y = y + dy
                    
                    if (temp_x, temp_y) not in obstacles_set:
                        x = temp_x
                        y = temp_y
                        c -= 1
                    else:
                        break
                    
                max_dist = max(max_dist, x*x + y*y)
        
        return max_dist
                    






        
