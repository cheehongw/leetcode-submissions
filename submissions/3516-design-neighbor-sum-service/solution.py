class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.N_ROWS = len(grid)
        self.N_COLS = len(grid[0])
        self.position = {}
        for row in range(self.N_ROWS):
            for col in range(self.N_COLS):
                val = grid[row][col]
                self.position[val] = (row, col)

    def adjacentSum(self, value: int) -> int:
        row, col = self.position[value]

        top = self.grid[row - 1][col] if row - 1 >= 0 else 0
        bot = self.grid[row + 1][col] if row + 1 < self.N_ROWS else 0
        left = self.grid[row][col-1] if col - 1 >= 0 else 0
        right = self.grid[row][col + 1] if col + 1 < self.N_COLS else 0
        # print(value, top, bot, left, right)

        return top + bot + left + right
        

    def diagonalSum(self, value: int) -> int:
        row, col = self.position[value]

        top_left = self.grid[row - 1][col - 1] if row - 1 >= 0 and col - 1 >= 0 else 0
        top_right = self.grid[row - 1][col + 1] if row - 1 >= 0 and col + 1 < self.N_COLS else 0
        bot_left = self.grid[row + 1][col - 1] if row + 1 < self.N_ROWS and col - 1 >= 0 else 0
        bot_right = self.grid[row + 1][col + 1] if row + 1 < self.N_ROWS and col + 1 < self.N_COLS else 0
        # print(value, top_left, top_right, bot_left, bot_right)

        return top_left + top_right + bot_left + bot_right


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
