class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        nums.append(0)

        elems_in_sub_array = {}
        number_of_unique = 0
        curr_sum = 0
        
        for i in range(k):
            elem = nums[i]
            if elem not in elems_in_sub_array:
                number_of_unique += 1
            
            elems_in_sub_array[elem] = elems_in_sub_array.get(elem, 0) + 1
            curr_sum += elem
        
        largest = 0

        for i in range(n - k + 1):
            if number_of_unique == k:
                largest = max(largest, curr_sum)
            
            elem_to_remove = nums[i]
            elems_in_sub_array[elem_to_remove] -= 1
            curr_sum -= elem_to_remove

            if elems_in_sub_array[elem_to_remove] == 0:
                number_of_unique -= 1

            elem_to_add = nums[k + i]
            elems_in_sub_array[elem_to_add] = elems_in_sub_array.get(elem_to_add, 0) + 1
            curr_sum += elem_to_add

            if elems_in_sub_array[elem_to_add] == 1:
                number_of_unique += 1

        return largest
