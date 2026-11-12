class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # s[i] = max subarray ending at and including index i

        # s[i] = (sum up to i) - (minimum prefix sum up to i-1)

        # answer is max(s)

        # can space optimize this

        
        s = []
        prefix = 0
        min_current_prefix = 0

        for num in nums:
            prefix += num
            s.append(prefix - min_current_prefix)
            min_current_prefix = min(min_current_prefix, prefix)

        return max(s)



