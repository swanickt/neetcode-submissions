class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        s = [[0] * n for _ in range(m)] # create an mxn array of zeroes

        for i in range(m):
            s[i][0] = 1
        
        for i in range(n):
            s[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths = 0

                if i > 0:
                    paths += s[i-1][j]
                
                if j > 0:
                    paths += s[i][j-1]
                
                s[i][j] += paths
        
        return s[m-1][n-1]