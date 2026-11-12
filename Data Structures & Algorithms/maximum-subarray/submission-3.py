class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # s[i] = max subarray ending at and including index i

        # s[i] = (sum up to i) - (minimum prefix sum up to i-1)

        # answer is max(s)

        # can space optimize this

        
        current_best = nums[0]
        prefix = nums[0]
        min_current_prefix = min(0, nums[0])

        for i in range(1, len(nums)):
            prefix += nums[i]
            current_best = max(current_best, prefix - min_current_prefix)
            min_current_prefix = min(min_current_prefix, prefix)

        return current_best



