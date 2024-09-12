class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set([c for c in allowed])

        count = 0
        for word in words:

            count += 1
            for c in word:
                if c not in allowed:
                    count -= 1
                    break

        return count
