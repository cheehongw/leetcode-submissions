class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        xs = [i for i in range(1, n+1)]
        ptr = 0
        players_left = n

        while(players_left > 1):
            moves = k - 1
            while (moves > 0):
                ptr = ptr + 1 if ptr + 1 < n else (ptr + 1) % n
                if xs[ptr] is None:
                    pass
                else:
                    moves -= 1
            
            xs[ptr] = None
            players_left -= 1
            
            while(True):
                ptr = ptr + 1 if ptr + 1 < n else (ptr + 1) % n
                if xs[ptr] is None:
                    pass
                else:
                    break

            
        return xs[ptr]
                
                
        
        
