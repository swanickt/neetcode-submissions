class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = 0
        R = len(nums) - 1

        while L < R:

            m = (L + R) // 2
# Compare the midpoint to the rightmost candidate; if mid is larger, the rotation minimum must be to its right.
            if nums[m] > nums[R]:
                L = m + 1
            else:
                R = m

        return nums[L]