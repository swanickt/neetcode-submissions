class Solution:
    def climbStairs(self, n: int) -> int:
        
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        
        # s = [1, 2]

        # for _ in range(3, n + 1):
        #     s.append(s[-1] + s[-2])
        
        # return s[-1]

        current, next = 1, 1 # (current, next) indices are (0, 1)

        for _ in range(n): # (current, next) indices are advanced n times
            current, next = next, next + current
        
        return current # (current, next) indices are (n, n+1)


