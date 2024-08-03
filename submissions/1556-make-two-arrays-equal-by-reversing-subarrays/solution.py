class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hashmap = {}

        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in target:
            hashmap[i] = hashmap.get(i, 0) - 1
            if hashmap[i] == 0:
                hashmap.pop(i)

        
        return not hashmap
