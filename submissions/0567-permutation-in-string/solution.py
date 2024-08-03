class Solution:

    # O(n) - time complexity
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # sliding window of len(s1) over s2
        hashmap = {}

        #add all chars of s1 into map
        for c in s1:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        def updateHashmap(c, isNewChar, hashmap):
            freq = hashmap.get(c, 0)
            freq = freq - 1 if isNewChar else freq + 1
            if freq == 0:
                hashmap.pop(c)
            else:
                hashmap[c] = freq

        l_ptr = 0
        r_ptr = len(s1) - 1

        for c in s2[l_ptr: r_ptr + 1]:
            updateHashmap(c, True, hashmap)

        if not hashmap:
            return True


        for r_ptr in range(len(s1), len(s2)):
            new_char = s2[r_ptr]
            removed_char = s2[l_ptr]
            l_ptr += 1

            updateHashmap(new_char, True, hashmap)
            updateHashmap(removed_char, False, hashmap)

            if not hashmap:
                return True

        return False

