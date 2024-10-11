class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        #O(2n) == O(n)
        events = []

        target_arrival = times[targetFriend][0]

        # O(n)
        for idx, t in enumerate(times):
            arrival, leaving = t[0], t[1]
            if arrival <= target_arrival:
                events.append((arrival, 1, idx))    # 1 to denote arrival
            
            if leaving <= target_arrival:
                events.append((leaving, 0, idx))    # 0 to denote leaving

        # we want to sort events by time. If happen at same time, 
        # leaving events should happen before arrivals 
        # O(nlogn)
        events.sort(key=lambda x: (x[0], x[1]))

        max_chair = 0
        heap = []
        chair_sat_by = {}

        #O(n)
        for e in events:
            time, isArrival, person_id = e
            if isArrival:
                if heap:
                    smallest_chair = heappop(heap)      #capped at log(n)
                    chair_sat_by[person_id] = smallest_chair
                else:
                    chair_sat_by[person_id] = max_chair
                    max_chair += 1

                if person_id == targetFriend:
                    return chair_sat_by[person_id]
            else:
                chair = chair_sat_by.pop(person_id)     
                heappush(heap, chair)                   #capped at log(n)



        
