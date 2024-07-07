class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numDrank = 0
        numEmpty = 0
        numFull = numBottles

        while True:
            numDrank += numFull
            no_of_bottles = numEmpty + numFull
            
            if (no_of_bottles >= numExchange):
                numFull = no_of_bottles // numExchange
                numEmpty = no_of_bottles % numExchange
            else:
                break

        return numDrank
        
