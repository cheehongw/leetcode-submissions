class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        

        def computeAns(prime):
            if prime == 2:
                return -1

            bitwise_repr = '0' + bin(prime)[2:]
            
            for x in range(len(bitwise_repr)):
                x_from_back = len(bitwise_repr) - 1 - x

                if (bitwise_repr[x_from_back] != '1'):
                    break

            
            
            result = bitwise_repr[:len(bitwise_repr) - x] + '0' + '1'* (x - 1)


            return int(result, 2)

        return [computeAns(p) for p in nums]

