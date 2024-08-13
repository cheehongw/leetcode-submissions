class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates.sort()

        def helper(c, t, curr_list, idx):
            if t < 0:
                return
            if t == 0:
                answer.append(curr_list)
                return
            for i in range(idx, len(c)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                helper(c, t - c[i], curr_list + [candidates[i]], i + 1)

        helper(candidates, target, [], 0)

        return answer
