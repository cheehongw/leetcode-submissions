class Solution:

    # O(n) time complexity
    # observation:
    # balanced string has all a's preceding b's
    # to make a string balance, remove all a's suceeding the first 'b' or
    # remove all b's preceding the first 'a'

    # to get minimum removal
    # for each index, count all the 'b's before it
    def minimumDeletions(self, s: str) -> int:

        countBs = [0]
        countSucceedingA = [0]
        

        for c in s:
            if c == 'b':
                countBs.append(countBs[-1] + 1)
            else:
                countBs.append(countBs[-1])
                countSucceedingA[0] += 1

        for c in s:
            if c == 'a':
                countSucceedingA[-1] -= 1
            
            countSucceedingA.append(countSucceedingA[-1])
                
            
        minDeletions = len(s)
        for i,c in enumerate(s):
            if c == 'a':
                minDeletions = min(minDeletions, countBs[i] + countSucceedingA[i])
            else:
                minDeletions = min(minDeletions, countSucceedingA[i] + countBs[i])

        return minDeletions


