class Solution:
    
    def maximumGain(self, s: str, x: int, y: int) -> int:
        final_points = 0
        if (x > y):
            s, points = self.removeABs(s, x)
            final_points += points
            s, points = self.removeBAs(s, y)
            final_points += points       

        else:
            s, points = self.removeBAs(s, y) 
            final_points += points       
            s, points = self.removeABs(s, x)
            final_points += points       


        return final_points
    
    def removeABs(self, s, x):
        stack = []
        points = 0
        for c in s:
            if (c == 'b' and stack and stack[-1] == 'a'):
                points += x
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack), points

    def removeBAs(self, s, y):
        stack = []
        points = 0
        for c in s:
            if (c == 'a' and stack and stack[-1] == 'b'):
                points += y
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack), points

