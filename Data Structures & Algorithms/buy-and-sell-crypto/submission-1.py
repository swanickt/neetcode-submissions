class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        min_price = prices[0] # min price seen so far (buy day)

        for i in range(1, len(prices)):
            
            potential_profit = prices[i] - min_price
           
            max_profit = max(max_profit, potential_profit)

            min_price = min(min_price, prices[i])

        return max_profit
        