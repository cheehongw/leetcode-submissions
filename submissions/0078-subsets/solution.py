class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        def subsetsRec(idx, nums):
            if idx == -1:
                return [[]]
            
            else:
                subresults = subsetsRec(idx - 1, nums)
                res = [ss + [nums[idx]] for ss in subresults]
                res.extend(subresults)

                return res
            
        
        return subsetsRec(len(nums) - 1, nums)


        ## alternative solution that uses backtracking:
        ## when generating the power set, we decide whether or not to include the 
        ## element at index i. This means that we will generate a binary tree of 
        ## decisions, with a depth of n: 
        ## - where the level i represents the decision to include the element i into the 
        ##   existing subset at that point in the tree
        ## - each point in the tree represents the possibility after taking a decision
        ##
        ## in this case, we terminate once we hit the required depth, which is i >= len(nums) 
        ## since all possible decisions have been exhausted.

        # res = []

        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
        #     # decision to include nums[i]
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     # decision NOT to include nums[i]
        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return res
