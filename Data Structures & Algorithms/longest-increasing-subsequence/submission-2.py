class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # s[i] = the longest strictly increasing subsequence ending at nums[i]

        # s[0] = 1

        # s[i] = 1 + max({s[j]: j < i and nums[j] < nums[i]} union {0}}

        # answer = max(s)

        s = [1]

        for i in range(1, len(nums)):

            best = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max (best, s[j])
            
            s.append(1 + best)

        return max(s)
