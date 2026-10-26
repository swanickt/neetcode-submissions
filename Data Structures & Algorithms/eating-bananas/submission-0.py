import math

class Solution:

    def validEatingSpeed(self, piles: List[int], h: int, speed: int) -> bool:

        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        
        if hours <= h:
            return True

        return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Can binary search over the possible options.
        # we know the min (i.e., k) will be <= max values in piles
        
        upper_bound = max(piles)
        lower_bound = 1

        while lower_bound < upper_bound:
            
            m = (lower_bound + upper_bound) // 2

            if self.validEatingSpeed(piles, h, m):
                upper_bound = m

            else:
                lower_bound = m + 1
        
        return lower_bound





