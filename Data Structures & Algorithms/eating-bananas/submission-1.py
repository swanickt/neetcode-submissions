import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # min k is no more than max pile size

        L = 1 # k at least 1
        R = max(piles)

        # binary search for the minimum possible

        while L < R:

            m = (L + R) // 2

            time = sum(math.ceil(pile / m) for pile in piles)

            if time <= h:
                R = m
            
            else:
                L = m + 1
        
        return L