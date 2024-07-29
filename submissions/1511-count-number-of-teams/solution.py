class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total_teams = 0
        
        for i, r in enumerate(rating):
            leftLessThanR = 0
            leftMoreThanR = 0

            rightLessThanR = 0
            rightMoreThanR = 0

            for j in range(len(rating)):
                if j < i:
                    leftLessThanR += 1 if rating[j] < r else 0
                    leftMoreThanR += 1 if rating[j] > r else 0
                elif j > i:
                    rightLessThanR += 1 if rating[j] < r else 0
                    rightMoreThanR += 1 if rating[j] > r else 0
            
            num_teams = (leftLessThanR * rightMoreThanR) + (leftMoreThanR * rightLessThanR)
            total_teams += num_teams

        return total_teams


