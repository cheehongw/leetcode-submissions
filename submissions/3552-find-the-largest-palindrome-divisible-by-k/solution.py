class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1 or k == 3 or k == 9:
            return "9"*n
        elif (k == 2):
            if (n == 1):
                return '8'
            elif (n == 2):
                return '88'
            else:
                return '8' + '9'*(n-2) + '8'
        elif (k == 4):
            if (n == 1):
                return '8'
            elif (n == 2):
                return '88'
            elif (n == 3):
                return '888'
            elif (n == 4):
                return '8888'
            else:
                return '88' + '9'*(n-4) + '88'
        elif (k == 5):
            if (n == 1):
                return '5'
            elif (n == 2):
                return '55'
            else:
                return "5" + "9"*(n - 2) + "5"
        
        elif (k == 8):
            if (1 <= n <= 5):
                return "8" * n
            else:
                return "888" + "9"*(n-6) + "888"
        
        elif (k == 6):
            if n == 1: return '6'
            elif n == 2: return '66'
            elif n == 3: return "888"
            elif n == 4: return "8778"
            else:
                something = ""
                if (n % 2 == 1):
                    something = ("9" * ((n - 5)//2)) + "8" + ("9" * ((n - 5)//2))
                else:
                    something = ("9" * ((n - 6)//2)) + "77" + ("9" * ((n - 6)//2))

                return "89" + something + "98"
        
        elif k == 7:
            if (1 <= n % 12 <= 6):
                if n % 12 == 1 or n % 12 == 5:
                    x = (n - 1) //2
                    return "9"*x + "7" + "9"*x
                elif n % 12 == 2 or n % 12 == 4:
                    x = (n - 2) //2
                    return "9"*x + "77" + "9"*x
                elif n % 12 == 3:
                    x = (n - 3) // 2
                    return "9"*x + "959" + "9"*x
                else:
                    return "9"*n
            else:
                if n % 12 == 7 or n % 12 == 11:
                    x = (n - 1) //2
                    return "9"*x + "4" + "9"*x
                elif n % 12 == 8 or n % 12 == 10:
                    x = (n - 2) //2
                    return "9"*x + "44" + "9"*x
                elif n % 12 == 9:
                    x = (n - 3) // 2
                    return "9"*x + "969" + "9"*x
                else:
                    return "9"*n
