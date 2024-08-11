class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        m = {
            'UP': -n,
            "RIGHT": 1,
            "LEFT": -1,
            "DOWN": n
        }

        pos = 0
        for c in commands:
            pos += m[c]

        return pos
        
