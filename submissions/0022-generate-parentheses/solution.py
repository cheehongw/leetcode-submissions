class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def helper(opened, closed):
            
            if (opened == closed and closed == n):
                res.append(''.join(stack))
                return
            if (opened > closed):
                stack.append(')')
                helper(opened, closed + 1)
                stack.pop()
            
            if (opened < n):
                stack.append('(')
                helper(opened + 1, closed)
                stack.pop()

        helper(0, 0)

        return res
