class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        curr_pos_sum = 0
        curr_neg_sum = 0
        num_negs = 0
        smallest_abs = 10**6

        for row in matrix:
            for elem in row:
                if elem < 0:
                    curr_neg_sum += elem
                    smallest_abs = min(abs(elem), smallest_abs)
                    num_negs += 1
                
                if elem >= 0:
                    curr_pos_sum += elem
                    smallest_abs = min(elem, smallest_abs)

        
        if num_negs % 2 == 0:
            return curr_pos_sum - curr_neg_sum
        else:
            return curr_pos_sum - curr_neg_sum - 2 * smallest_abs
                    





        
