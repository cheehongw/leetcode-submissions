class Solution:
    def minimumPushes(self, word: str) -> int:
        freqs = {}

        for c in word:
            freqs[c] = freqs.get(c, 0) + 1
        
        letters = sorted(freqs.items(), key=lambda tup:tup[1], reverse=True)
        
        pushes = 0
        numpad = 0
        for letter, count in letters:
            pushes_per_letter = (numpad // 8) + 1
            pushes += pushes_per_letter * count
            numpad += 1

        return pushes


        
