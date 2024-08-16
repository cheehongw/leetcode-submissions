class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        biggest = [-9999999, None]
        second_biggest = [-9999999, None]

        smallest = [9999999, None]
        second_smallest = [9999999, None]

        def update_biggest(new_num, idx):
            nonlocal biggest, second_biggest

            temp = [0, 0]


            temp[0] = min(new_num, biggest[0])
            temp[1] = idx if new_num <= biggest[0] else biggest[1]

            t = biggest[0]
            biggest[0] = max(new_num, biggest[0])
            biggest[1] = idx if new_num > t else biggest[1]

            t = second_biggest[0]
            second_biggest[0] = max(temp[0], second_biggest[0])
            second_biggest[1] = temp[1] if temp[0] > t else second_biggest[1]

        def update_smallest(new_num, idx):
            nonlocal smallest, second_smallest
            temp = [0, 0]


            temp[0] = max(new_num, smallest[0])
            temp[1] = idx if new_num >= smallest[0] else smallest[1]

            t = smallest[0]
            smallest[0] = min(small, smallest[0])
            smallest[1] = idx if new_num < t else smallest[1]
            
            t = second_smallest[0]
            second_smallest[0] = min(temp[0], second_smallest[0])
            second_smallest[1] = temp[1] if temp[0] < 1 else second_smallest[1]           

        for i, arr in enumerate(arrays):
            small = arr[0]
            big = arr[len(arr) - 1]
            
            update_biggest(big, i)
            update_smallest(small, i)
            # print(small, smallest, second_smallest)
            # print(big, biggest, second_biggest)


        if (biggest[1] == smallest[1]):
            return max(abs(biggest[0] - second_smallest[0]), abs(second_biggest[0] - smallest[0]))
        else:
            return abs(biggest[0] - smallest[0])
            
        
