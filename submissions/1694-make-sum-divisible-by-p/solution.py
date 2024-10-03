class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # sum the arr - get the modulo we need to remove
        # this is at least O(n), since we need to get the total sum
        # we can also compute prefix sums in O(1) time
        
        # for each position in the array, we know:
        # - the sum up to that point == how much removing this will affect the modulo
        # - how much more to remove to hit modulo 0

        total_sum = sum(nums)

        if total_sum % p == 0:
            return 0

        hashmap = {0: 0}
        
        curr_sum = 0
        min_len = len(nums)
        for i, num in enumerate(nums):
            curr_sum += num
            modulo = curr_sum % p
            needed = (p - ((total_sum - curr_sum) % p)) % p

            if (needed in hashmap):
                min_len = min(min_len, i + 1 - hashmap[needed])

            hashmap[modulo] = i + 1
        
        print(hashmap)
        return -1 if min_len == len(nums) else min_len

        



