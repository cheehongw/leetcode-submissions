class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            col = len(row)
            rightmost_pos = col - 1
            for i in range(col - 1, -1, -1):
                elem = row[i]
                if elem == ".":
                    continue

                if elem == "#":
                    row[i] = "."
                    row[rightmost_pos] = "#"
                    rightmost_pos = rightmost_pos - 1
                
                if elem == "*":
                    rightmost_pos = i - 1
        
        matrix = [[None] * len(box) for _ in range(len(box[0]))]

        for i, row in enumerate(box):
            for j, elem in enumerate(row):
                matrix[j][len(box) - i - 1] = elem

        return matrix


        
