class Solution:
    def possibleStringCount(self, word: str) -> int:
        curr_char = ''
        possbl = 1

        
        for c in word:
            if curr_char == c:
                possbl += 1

            else:
                curr_char = c

        return possbl
