class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [arr[0]]*len(arr)
        for i in range(1, len(arr)):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]
            

        answer = [0]*len(queries)
        for i, query in enumerate(queries):
            l, r = query[0], query[1]

            if l - 1 >= 0:
                answer[i] = prefix_xor[r] ^ prefix_xor[l - 1]
            else:
                answer[i] = prefix_xor[r]

        
        return answer



        
