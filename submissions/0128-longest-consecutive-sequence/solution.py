class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashmap: number -> range of sequence containing it
        
        consec_seq_map = {}

        for num in nums:
            if num in consec_seq_map:
                continue
            else:
                num_before = num - 1
                num_after = num + 1
                lowest_range = num
                largest_range = num

                range_num_before = consec_seq_map.get(num_before, None)
                range_num_after = consec_seq_map.get(num_after, None)
                
                #find the curr lower limit of num
                if range_num_before is None:
                    pass
                else:
                    lowest_range = range_num_before[0]
                    
                if range_num_after is None:
                    #found the curr upper limit with num
                    pass                    
                else:
                    largest_range = range_num_after[1]

                consec_seq_map[lowest_range] = (lowest_range, largest_range)
                consec_seq_map[largest_range] = (lowest_range, largest_range)
                if (range_num_before is not None):
                    consec_seq_map[num_before] = (lowest_range, largest_range)
                if (range_num_after is not None):
                    consec_seq_map[num_after] = (lowest_range, largest_range)
                consec_seq_map[num] = (lowest_range, largest_range)

        longest_length = 0
        for ranges in consec_seq_map.values():
            # print(ranges)
            if ranges is not None:
                lower, upper = ranges
                length = upper - lower + 1

                longest_length = length if length > longest_length else longest_length

        
        return longest_length


                    
                    
                    


        
