class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_skill = sum(skill)
        n_teams = len(skill) // 2
        skill_per_team = total_skill // n_teams

        if total_skill % n_teams != 0:
            return -1
        
        hashmap = {}
        chem = 0

        for sk in skill:
            other_skill_lvl = skill_per_team - sk
            if other_skill_lvl in hashmap:
                hashmap[other_skill_lvl] -= 1
                if hashmap[other_skill_lvl] == 0:
                    hashmap.pop(other_skill_lvl)

                chem += sk * other_skill_lvl
            else:
                hashmap[sk] = hashmap.get(sk, 0) + 1
        
        if hashmap.items():
            return -1
        
        return chem

