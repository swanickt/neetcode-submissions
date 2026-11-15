class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2:
            return False
        
        half = total // 2

        # problem is equivalent to the existence of a subset totalling half

        # s[i][j] = True or False (existence of subset of nums[:i] totalling j)

        # answer is s[n][half] for n = len(nums)

        # half > 0, so s[0][j] for j>=1 is False

        # s[i][0] is true (empty subset totals zero)

        n = len(nums)

        s = [[False] * (half + 1) for _ in range(n+1)]

        for i in range(n+1):
            s[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, half + 1):

                # either the subset contains the ith element or not

                if j - nums[i-1] >= 0 and s[i-1][j-nums[i-1]]:
                    s[i][j] = True
                
                elif s[i-1][j]:
                    s[i][j] = True
        
        return s[n][half]