class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()

        word_count = {}

        words1.extend(words2)
        for w in words1:
            word_count[w] = word_count.get(w, 0) + 1
        
        
        uncommon = []
        for k,v in word_count.items():
            if v == 1:
                uncommon.append(k)


        return uncommon
        
        
