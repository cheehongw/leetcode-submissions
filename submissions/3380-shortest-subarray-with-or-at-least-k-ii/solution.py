class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit_count = [0] * 32
        l_ptr, r_ptr = 0, 1
        res = 99999999999999999

        def current_window():
            val = 0
            for i in bit_count:
                val <<= 1
                if i > 0:
                    val = val | 1
            return val

        def update_bitcounts(val, is_add):
            
            bit = 31
            while val:
                if val & 1 == 1:
                    bit_count[bit] = bit_count[bit] + 1 if is_add else bit_count[bit] - 1
                
                val >>= 1
                bit -= 1
    
        update_bitcounts(nums[0], True)

        while l_ptr < r_ptr:
            if current_window() < k and r_ptr < len(nums):
                r_ptr += 1
                # update bitcounts
                update_bitcounts(nums[r_ptr - 1], True)
            # else incr l_ptr
            elif current_window() >= k:
                res = min(res, r_ptr - l_ptr)
                l_ptr += 1
                update_bitcounts(nums[l_ptr - 1], False)
            else:
                break

        return -1 if res == 99999999999999999 else res

