class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k == 0:
            return 0
        
        count = 0

        L = 0

        prod = 1

        for R, num in enumerate(nums):
            prod *= num
            
            while L < R and prod >= k:
                prod /= nums[L]
                L += 1
            
            if prod < k:
                count += (R-L+1)
            
        return count

