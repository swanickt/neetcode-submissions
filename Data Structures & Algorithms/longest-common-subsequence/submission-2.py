class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # s[i, j] = longest common subsequence between text1[:i] and text2[:j]

        m = len(text1)
        n = len(text2)

        # answer = s[m - 1][n - 1]

        s = [[0]*n for _ in range(m)] 

        # s[i, j]

        for i in range(m):
            for j in range(n):
                longest = 0
                if text1[i] == text2[j]:
                    longest = 1
                    if i-1 >= 0 and j-1 >= 0:
                        longest += s[i-1][j-1]
                    
                else:
                    longest = 0
                    if i - 1 >= 0:
                        longest = s[i-1][j]
                    if j-1 >= 0:
                        longest = max(longest, s[i][j-1])
    
                
                s[i][j] = longest
        
        return s[m-1][n-1]
                
            
            
