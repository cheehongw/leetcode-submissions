class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        one_pass_chalk_use = sum(chalk)

        k = k % one_pass_chalk_use

        for idx, chalk_used in enumerate(chalk):
            if k < chalk_used:
                return idx
            
            k -= chalk_used
