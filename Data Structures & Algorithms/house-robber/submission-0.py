class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # s[i] = max amount of money we can rob from houses 0, ..., i

        # Either we rob the ith house, or we don't. If we don't, 
        # s[i] = s[i-1]. Else, s[i] = nums[i] + s[i-2]

        # Then, s[i] = max{s[i-1], nums[i] = s[i-2]}

        s = [nums[0]]
        
        if len(nums) == 1:
            return s[0]
        
        s.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            s.append(max(s[i-1], nums[i] + s[i-2]))
        
        return s[-1]
        