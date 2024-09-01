class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def getColor(coord):
            letter1 = coord[0]
            letter2 = coord[1]

            if ((ord(letter1) - ord('a')) % 2 == 0 and int(letter2) % 2 == 1):
                return 'black'
            
            if ((ord(letter1) - ord('a')) % 2 == 1 and int(letter2) % 2 == 0):
                return 'black'

            return 'white'

        print(getColor(coordinate1), getColor(coordinate2))
        return getColor(coordinate1) == getColor(coordinate2)
