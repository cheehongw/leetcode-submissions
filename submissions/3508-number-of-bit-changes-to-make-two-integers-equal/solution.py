class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # 1101 vs 0100
        # 1110 vs 0001

        n_bin = "{0:b}".format(n)
        k_bin = "{0:b}".format(k)

        idx_k = len(k_bin) - 1
        changes = 0
        for i in range(len(n_bin) - 1, -1, -1):
            k_bigit = k_bin[idx_k] if idx_k >= 0 else '0'
            print(n_bin[i], k_bigit)
            if (n_bin[i] == k_bigit):
                pass
            elif(k_bigit == '1'):
                return -1
            else:
                changes += 1

            idx_k -= 1

        if (idx_k >= 0):
            return -1

        return changes



            
