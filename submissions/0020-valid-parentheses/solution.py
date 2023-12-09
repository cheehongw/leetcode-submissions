class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis_map = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for i in range(len(s)):
            char = s[i]            
            if (char in parenthesis_map):
                stack.append(char)
            else: #closing bracket
                if len(stack) == 0:
                    return False

                bracket = stack.pop()
                if parenthesis_map[bracket] != char:
                    return False

        if len(stack) > 0:
            return False

        return True


        
