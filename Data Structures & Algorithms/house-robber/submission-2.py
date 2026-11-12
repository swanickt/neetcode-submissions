class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # s[i] = most money we can rob from houses 0, ..., i
        # s[0] = nums[0]
        # s[1] = max(nums[0], nums[1])

        # s[i] = max(s[i-1], nums[i] + s[i-2])

        # answer: s[n] 

        s = [nums[0]]

        if len(nums) == 1:
            return s[-1]
        
        s.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            s.append(max(s[i-1], nums[i] + s[i-2]))
        
        return s[-1]



        