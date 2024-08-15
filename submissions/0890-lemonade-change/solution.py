class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        bill_count = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            bill_count[bill] += 1

            if (bill == 10):
                bill_count[5] -= 1
                if bill_count[5] < 0:
                    return False
            
            if (bill == 20):
                bill_count[20] += 1
                
                if (bill_count[10] > 0 and bill_count[5] > 0):
                    bill_count[10] -= 1
                    bill_count[5] -= 1
                elif (bill_count[5] >= 3):
                    bill_count[5] -= 3
                else:
                    return False
        
        return True
