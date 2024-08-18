class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        lastHour = len(energyDrinkA)
        memoA = [None] * lastHour
        memoB = [None] * lastHour
        
        def maxEnBoost(hour, prevDrank):
            if hour >= lastHour:
                return 0

            if prevDrank == 'A':
                if memoA[hour] is not None:
                    return memoA[hour]
            else:
                if memoB[hour] is not None:
                    return memoB[hour]

            
            if prevDrank == 'A':
                drinkA = energyDrinkA[hour] + maxEnBoost(hour + 1, 'A')
                drinkB = 0 + maxEnBoost(hour + 1, 'B')

                memoA[hour] = max(drinkA, drinkB)
                return memoA[hour]
            else:
                drinkA = 0 + maxEnBoost(hour + 1, 'A')
                drinkB = energyDrinkB[hour] + maxEnBoost(hour + 1, 'B')
                
                memoB[hour] = max(drinkA, drinkB)
                return memoB[hour]

        return max(maxEnBoost(1, 'A') + energyDrinkA[0], maxEnBoost(1, 'B') + energyDrinkB[0])

