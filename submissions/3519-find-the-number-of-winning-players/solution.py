class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        
        players = {}
        winners = set()

        for p in pick:
            player, color = p[0], p[1]
            if (player in winners):
                continue

            picked_balls = players.get(player, {})

            picked_balls[color] = picked_balls.get(color, 0) + 1
            if picked_balls[color] > player:
                winners.add(player)
            
            players[player] = picked_balls

        return len(winners)

        
