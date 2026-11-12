class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dynamic programming
        # s[i] = longest strictly increasing subsequence ending at and  
        #        including s[i]
        #
        # s[i] = 1 + max{s[j] : j < i and nums[j] < nums[i]}


        # answer: max(s)

        s = [1]

        for i in range(1, len(nums)):
            current_max = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    current_max = max(1 + s[j], current_max)
            
            s.append(current_max)
        
        return max(s)


