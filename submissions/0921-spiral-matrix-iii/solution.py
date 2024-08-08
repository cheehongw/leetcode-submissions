class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        NUM_ELEMS = rows * cols

        coords = [[rStart, cStart]]

        dir = 'east'
        steps_to_take = 1
        steps = 1

        row = rStart
        col = cStart

        while (len(coords) < NUM_ELEMS):
            if (dir == 'east'):
                row, col = row, col + 1
            elif (dir == 'south'):
                row, col = row + 1, col
            elif (dir == 'west'):
                row, col = row, col - 1
            elif (dir == 'north'):
                row, col = row - 1, col


            if 0 <= row < rows and 0 <= col < cols:
                coords.append([row, col])
                
            steps -= 1
            if (steps == 0):
                if (dir == 'east'):
                    dir = 'south'
                    steps = steps_to_take
                elif (dir == 'south'):
                    dir = 'west'
                    steps_to_take += 1
                    steps = steps_to_take
                elif (dir == 'west'):
                    dir = 'north'
                    steps = steps_to_take
                elif (dir == 'north'):
                    dir = 'east'
                    steps_to_take += 1
                    steps = steps_to_take

        return coords

        
