class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = [0] * (len(nums) - k + 1)

        l_ptr = 0
        r_ptr = 0
        
        is_consec = [False] * (len(nums) - 1)
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1] - 1):
                is_consec[i] = True
        
        for l_ptr in range(len(nums) - k + 1):
            is_true = True

            if (r_ptr < l_ptr):
                r_ptr = l_ptr

            while (r_ptr - l_ptr != k - 1):
                if (not is_consec[r_ptr]):
                    is_true = False
                    break
                r_ptr += 1

            if is_true:
                results[l_ptr] = nums[r_ptr]
            else:
                results[l_ptr] = -1

        
        return results



                     
        
