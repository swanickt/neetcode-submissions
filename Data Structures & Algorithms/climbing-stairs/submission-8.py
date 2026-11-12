class Solution:
    def climbStairs(self, n: int) -> int:
        """
        current, next = 1, 1 # (current, next) indices are (0, 1)

        for _ in range(n): # (current, next) indices are advanced n times
            current, next = next, next + current
        
        return current # (current, next) indices are (n, n+1)
        """
        # s[i] is the number of distinct ways to climb to step i
        # In general, s[i] = s[i-1] + (s[i-2])
        # Base cases: s[1] = 1, s[2] = 2

        # Answer: s[n]

        """
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        s = [1, 2]

        for _ in range(3, n+1):
            s.append(s[-1] + s[-2])
        
        return s[-1]
        """
        
        """
        If the table-based solution is more intuitive, use that initially. In a coding interview, a correct 
        (O(n)\)-time, \(O(n)\)-space solution is a perfectly good starting point. You can then 
        explain that each state depends only on its two predecessors and reduce the space to \(O(1)\).
        """

        # to do this without a table (i.e., 2 variables to reduce the memory to O(1)), 
        # maintain two pointers, back_2, and back_1

        # s[i] = number of ways to reach step i
        # s[i] = s[i-1] + s[i-2]
        # Base cases: s[0] = 1, s[1] = 1

        # Initially, current_ways = s[0], next_ways = s[1]
        current_ways, next_ways = 1, 1

        # At each iteration:
        #   current_ways = s[i]
        #   next_ways = s[i+1]
        #
        # Shift forward by one step:
        #   new current_ways = s[i+1]
        #   new next_ways = s[i] + s[i+1] = s[i+2]
        for _ in range(n):
            current_ways, next_ways = next_ways, next_ways + current_ways
        
        return current_ways


