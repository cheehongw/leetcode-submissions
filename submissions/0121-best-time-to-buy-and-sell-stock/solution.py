class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        lowestPriceSeen = None
        
        for price in prices:
            if lowestPriceSeen is None or price < lowestPriceSeen:
                lowestPriceSeen = price
            
            bestProfit = max(price - lowestPriceSeen, bestProfit)
            
        return bestProfit
