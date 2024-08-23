class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        frac_1 = '0/1'
        frac_2 = ''
        ope = '+'
        
        for i,c in enumerate(expression):

            if ((c == '-' or c == '+')):
                if (frac_2 != ''):
                    frac_1 = self.fraction_add(frac_1, frac_2, ope)
                    frac_2 = ''

                ope = c 

            else:
                frac_2 += c

        frac_1 = self.fraction_add(frac_1, frac_2, ope)
        return frac_1

        
    def fraction_add(self, frac1, frac2, operation):
        print(frac1, frac2, operation)
        num1, den1 = frac1.split('/')
        num1, den1 = int(num1), int(den1)
        num2, den2 = frac2.split('/')
        num2, den2 = int(num2), int(den2)
        
        result_num = 0
        result_den = den1 * den2

        if (operation == '+'):
            result_num = num1*den2 + num2*den1
        else:
            result_num = num1*den2 - num2*den1

        g = gcd(result_num, result_den)
        
        result_num = result_num // g
        result_den = result_den // g
        if (result_den < 0):
            result_den = abs(result_den)
            result_num *= -1

        return f'{str(result_num)}/{str(result_den)}'

