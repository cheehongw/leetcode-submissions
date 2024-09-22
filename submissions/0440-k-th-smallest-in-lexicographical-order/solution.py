class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        length_n = len(str(n))
        
        total_count = 0

        def count_lexicographically(prefix, n):
            print(prefix)
            num_digits_n = len(str(n))
            num_digits_prefix = len(str(prefix))
            
            if prefix == n:
                return 1
            
            if prefix > n:
                return 0

            count = 1

            diff = num_digits_n - num_digits_prefix

            if diff > 0:
                max_with_prefix = prefix * (10**diff) + int('9'*diff)
                min_with_prefix = prefix * (10**diff)
                if max_with_prefix < n:
                    return int('1'*(diff + 1))

                if n < min_with_prefix:
                    return int ('1' * diff)

                 

            for i in range(0, 10): 
                count += count_lexicographically(prefix*10 + i, n)

            return count
        
        first_loop = True
        prefix = 0
        while True:
            begin = 1 if first_loop else 0
            for i in range(begin, 10):
                prefix_under_test = prefix + i
                if total_count + 1 == k:
                    return prefix_under_test

                count = count_lexicographically(prefix_under_test, n)
                
                if k <= total_count + count:
                    prefix = prefix_under_test * 10
                    total_count += 1
                    break
                else:
                    total_count += count
            
            first_loop = False
        
        
        return prefix
        

