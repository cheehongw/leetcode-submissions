class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        expected_total = mean * (n + len(rolls))
        curr_total = sum(rolls)

        remaining_total = expected_total - curr_total

        if (n <= remaining_total <= n*6) :
            base_value = remaining_total // n
            remainder = remaining_total % n

            res = [base_value]*n
            for i in range(remainder):
                res[i] += 1

            return res

        else:
            return []
        
