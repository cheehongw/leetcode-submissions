class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        # maxScore = max(maxScore(future choice #...) + choice of score)

        memo = [[None] * n for _ in range(k + 1)]
        
        def dp(days_left, curr_city):
            if memo[days_left][curr_city]:
                return memo[days_left][curr_city]
            
            if days_left == 1:
                memo[days_left][curr_city] = max(stayScore[k - days_left][curr_city], max(travelScore[curr_city]))
                return memo[days_left][curr_city]
            else:
                #choice from staying in curr_city
                max_score = stayScore[k - days_left][curr_city] + dp(days_left - 1, curr_city)
                
                for dest_city in range(n):
                    if dest_city == curr_city:
                        pass

                    max_score = max(max_score, travelScore[curr_city][dest_city] + dp(days_left - 1, dest_city))

                memo[days_left][curr_city] = max_score

                return memo[days_left][curr_city]

        highest = 0
        for start in range(n):
            highest = max(highest, dp(k, start))

        return highest
