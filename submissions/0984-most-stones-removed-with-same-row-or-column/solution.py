class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parents = {}
        row = {}
        col = {}


        def findParent(stone):
            if parents[stone] == stone:
                return stone
            
            parents[stone] = findParent(parents[stone])
            return parents[stone]


        for stone in stones:
            x, y = stone[0], stone[1]
            hashable_stone = (x,y)
            parents[hashable_stone] = hashable_stone    
            if x in row or y in col:
                if x in row:
                    prev_row_parent = findParent(row[x])
                    parents[prev_row_parent] = hashable_stone
                                
                if y in col:
                    prev_col_parent = findParent(col[y])
                    parents[prev_col_parent] = hashable_stone

            row[x] = hashable_stone
            col[y] = hashable_stone

    

        top_level_pars = set()

        # print(parents)

        for stone in stones:
            hashable_stone = (stone[0], stone[1])
            top_level_pars.add(findParent(hashable_stone))

        return len(stones) - len(top_level_pars)


