class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        s = [1, 2]

        for _ in range(3, n + 1):
            s.append(s[-1] + s[-2])
        
        return s[-1]



