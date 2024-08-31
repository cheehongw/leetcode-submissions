class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        def d1(num):
            return num // 1000

        def d2(num):
            return (num % 1000) // 100

        def d3(num):
            return (num % 100) // 10

        def d4(num):
            return (num % 10)

        digit_1 = min(d1(num1), d1(num2), d1(num3))
        digit_2 = min(d2(num1), d2(num2), d2(num3))
        digit_3 = min(d3(num1), d3(num2), d3(num3))
        digit_4 = min(d4(num1), d4(num2), d4(num3))

        int_str = int(str(digit_1) + str(digit_2) + str(digit_3) + str(digit_4))

        return int_str

