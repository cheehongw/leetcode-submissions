class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = [None] * len(days)
        
        def minCost(idx):
            
            if (idx >= len(days)):
                return 0

            if (memo[idx]):
                return memo[idx]
            
            idx_1_day_pass = idx + 1
            idx_7_day_pass = idx
            idx_30_day_pass = idx

            while (idx_7_day_pass < len(days) and days[idx_7_day_pass] < days[idx] + 7):
                idx_7_day_pass += 1
            
            while (idx_30_day_pass < len(days) and days[idx_30_day_pass] < days[idx] + 30):
                idx_30_day_pass += 1


            memo[idx] = min(
                minCost(idx_1_day_pass) + costs[0],
                minCost(idx_7_day_pass) + costs[1],
                minCost(idx_30_day_pass) + costs[2]
            )

            return memo[idx]

        return minCost(0)
            
