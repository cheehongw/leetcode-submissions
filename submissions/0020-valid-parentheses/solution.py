class Solution:
    def isValid(self, s: str) -> bool:
    
        bracket_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        
        stack = []

        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                if (len(stack) == 0):
                    return False
                check = stack.pop()
                if (check != bracket_map[c]):
                    return False
                
        
        return len(stack) == 0
        
