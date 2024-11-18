class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n

        if k > 0:
            curr_sum = sum(code[:k + 1])
            for i in range(n):
                curr_sum -= code[i]
                result[i] = curr_sum
                curr_sum += code[(i + k + 1) % n]
            
        if k < 0:
            curr_sum = sum(code[k:])
            for i in range(n):
                result[i] = curr_sum
                curr_sum += code[i]
                curr_sum -= code[(n + k + i) % n]
                # print(code[i], code[(n + k + i) % n])
        
        return result
