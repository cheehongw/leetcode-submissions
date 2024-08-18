class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        def count1(ss):
            count_1 = 0
            count_0 = 0
            for i in ss:
                if i == '1':
                    count_1 += 1
                else:
                    count_0 += 1
            
            return count_0, count_1
        

        count = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                c0, c1 = count1(s[i:j])
                # print(s[i:j])
                if c0 <= k or c1 <= k:
                    count += 1
        

        return count
        
