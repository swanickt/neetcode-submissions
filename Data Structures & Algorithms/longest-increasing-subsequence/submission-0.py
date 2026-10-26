class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dynamic programming
        # s[i] = longest strictly increasing subsequence ending at and  
        #        including s[i]
        #
        # s[i] = 1 + max{s[j] : j < i and nums[j] < nums[i]}

        s = []
        s.append(1)

        for i in range(1, len(nums)):
            
            curr_max = 0
            
            for j in range(0, i):
                
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, s[j])
            
            s.append(1 + curr_max)
        
        return max(s)

