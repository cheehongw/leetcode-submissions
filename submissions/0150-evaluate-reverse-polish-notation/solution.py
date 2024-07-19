class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()
            c = None

            if t == '+':
                c = a + b
            elif t == '-':
                c = a - b
            elif t == '*':
                c = a * b    
            elif t == '/':
                r = a / b
                c = floor(r) if r >=0 else ceil(r)

            stack.append(c)
        
        return stack[0]
