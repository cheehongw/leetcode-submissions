class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        converted = [0] * len(timePoints)

        for i, time in enumerate(timePoints):
            hhmm = time.split(":")
            hh = 60 * int(hhmm[0])
            mm = int(hhmm[1])

            converted[i] = hh + mm

        converted.sort()
        converted.append(converted[0] + 1440)
        
        minimum = 9999999
        for i in range(1, len(converted)):
            diff = converted[i] - converted[i - 1]
            minimum = min(diff, minimum)

        return minimum
            
            
