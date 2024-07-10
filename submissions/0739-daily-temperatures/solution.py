class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            answer = 0

            while(stack):
                next_days_temp, days = stack[-1]

                if next_days_temp <= temp:
                    answer += days
                    stack.pop()

                elif next_days_temp > temp:
                    stack.append((temp, answer + 1))
                    result[i] = answer + 1
                    break

            if not stack:
                stack.append((temp, 0))
                result[i] = 0
        
        return result
