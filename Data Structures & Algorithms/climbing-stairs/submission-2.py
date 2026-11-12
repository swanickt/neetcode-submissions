class Solution:
    def climbStairs(self, n: int) -> int:
        
        # s[i] is the number of distinct ways to climb to step i
        # In general, s[i] = s[i-1] + (s[i-2])
        # Base cases: s[1] = 1, s[2] = 2

        # Answer: s[n]

        if n == 1:
            return 1
        
        if n == 2:
            return 2
            
        s = [1, 2]

        for _ in range(3, n+1):
            s.append(s[-1] + s[-2])
        
        return s[-1]

        # to do this without a table (i.e., 2 variables to reduce the memory to O(1)), 
        # maintain 


