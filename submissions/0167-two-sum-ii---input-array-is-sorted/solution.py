class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr, r_ptr = 0, len(numbers) - 1

        while (True):
            sum = numbers[l_ptr] + numbers[r_ptr]
            if (sum == target):
                return [l_ptr + 1, r_ptr + 1]
            elif (sum > target):
                r_ptr -= 1
            elif (sum < target):
                l_ptr += 1



        
