class Solution:
    # O(n) time complexity
    # O(1) space complexity 
    def maxProfit(self, prices: List[int]) -> int:
        curr_max_profit = 0
        curr_lowest_price = None

        for i in range(len(prices)):
            price = prices[i]
            if (curr_lowest_price is None):
                curr_lowest_price = price
            else:
                curr_lowest_price = min(curr_lowest_price, price)
            curr_max_profit = max(price - curr_lowest_price, curr_max_profit)

        return curr_max_profit

