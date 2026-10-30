class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_profit = 0

        lowest_price_so_far = prices[0]

        for i in range(1, len(prices)):
            
            if prices[i] - lowest_price_so_far > best_profit:
                best_profit = prices[i] - lowest_price_so_far

            if prices[i] < lowest_price_so_far:
                lowest_price_so_far = prices[i]
        
        return best_profit


        