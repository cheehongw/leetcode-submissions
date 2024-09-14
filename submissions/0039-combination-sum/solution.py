class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # at each combi, we have the option of 
        # - exclude and move on
        # - include and move on
        # - include and stay
        
        res = []

        combi = []
        def dfs(idx, running_sum):    
            if (idx >= len(candidates)):
                return

            if (running_sum > target):
                return
            
            if running_sum == target:
                res.append(combi.copy())
                return

            combi.append(candidates[idx])
            dfs(idx, running_sum + candidates[idx])
            
            combi.pop()
            dfs(idx + 1, running_sum)     

                
        dfs(0, 0)
        return res

