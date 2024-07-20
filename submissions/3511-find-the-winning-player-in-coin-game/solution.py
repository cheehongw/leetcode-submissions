class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = True

        while(x >= 1 and y >= 4):
            x -= 1
            y -= 4

            turn = not turn

        return 'Alice' if not turn else 'Bob'
        
