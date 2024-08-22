class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        digits = 0
        while (temp):
            temp = temp >> 1
            digits += 1

        print(digits)
        max_num = (2**digits) - 1
        compl = max_num - num

        return compl
