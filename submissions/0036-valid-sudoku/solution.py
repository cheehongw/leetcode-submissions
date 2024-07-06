class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for row in range(9):
            for col in range(9):
                square = (row // 3)*3 + col // 3
                number = board[row][col]
                # print(f'number: {number}, row: {row}, col: {col}, square: {square}')

                if (number == '.'):
                    continue
                else:
                    if number in rows[row] or number in cols[col] or number in squares[square]:
                        return False
                    else:
                        rows[row].add(number)
                        cols[col].add(number)
                        squares[square].add(number)
        
        return True

