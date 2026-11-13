class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        s = [[0] * n for _ in range(m)]

        s[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

                if i-1 >= 0 and obstacleGrid[i-1][j] != 1:
                    s[i][j] += s[i-1][j]
                
                if j-1 >= 0 and obstacleGrid[i][j-1] != 1:
                    s[i][j] += s[i][j-1]
        
        return s[m-1][n-1]
        