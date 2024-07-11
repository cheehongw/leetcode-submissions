class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                reversed = collections.deque()
                while (True):
                    popped = stack[-1]
                    stack.pop()
                    if (popped == '('):
                        break
                    else:
                        reversed.append(popped)

                for x in reversed:
                    stack.append(x)
            
            else:
                stack.append(c)

        return ''.join(stack)   


        
