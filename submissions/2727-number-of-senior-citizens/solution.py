class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for det in details:
            age = det[11:13]
            count += 1 if int(age) > 60 else 0
        
        return count
