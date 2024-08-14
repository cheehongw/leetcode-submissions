class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def count_pairs_leq_d(d):
            l_ptr = 0
            count = 0
            
            for r_ptr in range(len(nums)):
                
                while (nums[r_ptr] - nums[l_ptr] > d):
                    l_ptr += 1
                
                count += r_ptr - l_ptr

            return count
                


        largest_d = nums[-1]
        smallest_d = 0

        while (smallest_d < largest_d):

            midpoint_d = (largest_d + smallest_d) // 2

            pairs_leq_d = count_pairs_leq_d(midpoint_d)
            
            if (pairs_leq_d < k):
                smallest_d = midpoint_d + 1
            else:
                largest_d = midpoint_d

        return smallest_d
