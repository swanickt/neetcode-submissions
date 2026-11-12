class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # let s[i] be the max subarray of nums ending at index i 

        # s[i] = (sum to i) - (min prefix up to index i-1)

        # answer = max(s)

        current_prefix_sum = 0
        min_prefix = 0
        current_max = 0

        for i in range(len(nums)):
            
            current_prefix_sum += nums[i]
            if i == 0:
                current_max = nums[0]
            else:
                current_max = max(current_max, current_prefix_sum - min_prefix)
            
            min_prefix = min(min_prefix, current_prefix_sum)
        
        return current_max




