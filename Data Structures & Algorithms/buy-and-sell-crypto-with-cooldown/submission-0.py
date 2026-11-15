class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # At the end of each day, we can be in one of three situations

        # State	    Meaning
        #   holding	Maximum profit if we end today holding one share
        #   sold	Maximum profit if we sold a share today
        #   resting	Maximum profit if we end today without a share and did not sell today

        # Before day 0, we have no stock and profit 0.
        # Holding or having sold is initially impossible.
        
        dp_holding = float("-inf")
        dp_sold    = float("-inf")
        dp_resting = 0

        for price in prices:

            # dp_holding:
            dp_holding, dp_sold, dp_resting = (
                max(dp_holding, dp_resting - price), # hold or buy
                dp_holding + price, # sell
                max(dp_sold, dp_resting) # resting or cooldown

            )
        
        return max(dp_sold, dp_resting)



            


