class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        events = set()
        event_score = {}

        for interval in intervals:
            left, right = interval[0], interval[1]
            events.add(left)
            events.add(right + 0.5)

            event_score[left] = event_score.get(left, 0) + 1
            event_score[right + 0.5] = event_score.get(right + 0.5, 0) - 1
            

        event_list = list(events)
        event_list.sort()
        
        max_intersect = 0
        curr_intersect = 0

        for e in event_list:
            curr_intersect += event_score[e]
            max_intersect = max(max_intersect, curr_intersect)

        return max_intersect



        
