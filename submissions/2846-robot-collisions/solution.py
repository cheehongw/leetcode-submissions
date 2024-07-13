class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []

        for i in range(len(positions)):
            robot = (positions[i], healths[i], directions[i], i + 1)
            robots.append(robot)
    
        robots.sort(key= lambda robot : robot[0])
        
        stack = []
        for bot in robots:
            if (bot[2] == 'R'):
                stack.append(bot)
            elif (stack and stack[-1][2] == 'R'):
                #collide logic
                while (stack and stack[-1][2] == 'R' and bot[1] > stack[-1][1]):
                    stack.pop()
                    temp = list(bot)
                    temp[1] -= 1
                    bot = tuple(temp)
                if (stack and stack[-1][2] == 'R' and bot[1] <= stack [-1][1]):
                    if (stack[-1][1] == bot[1]):
                        stack.pop()
                    else:
                        stack[-1] = (stack[-1][0], stack[-1][1] - 1, stack[-1][2], stack[-1][3])
                elif ((stack and stack[-1][2] == 'L') or (not stack)):
                    stack.append(bot)
            else:
                stack.append(bot)
        
        stack.sort(key= lambda robot : robot[3])
        return [bot[1] for bot in stack]





                

        

        
