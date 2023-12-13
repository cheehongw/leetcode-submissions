from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        LRTB = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(image)
        n = len(image[0])

        coordinates = deque([])
        coordinates.append((sr, sc))
        while(len(coordinates) != 0):
            coords = coordinates.popleft()
            if image[coords[0]][coords[1]] == color:
                continue
            

            for dir in LRTB:
                newPosX = coords[0] - dir[0]
                newPosY = coords[1] - dir[1]
                if (newPosX < 0 or newPosX >= m):
                    continue
                
                if (newPosY < 0 or newPosY >= n):
                    continue

                if (image[newPosX][newPosY] != image[coords[0]][coords[1]]):
                    continue

                coordinates.append((newPosX, newPosY))

            image[coords[0]][coords[1]] = color

        return image
            
