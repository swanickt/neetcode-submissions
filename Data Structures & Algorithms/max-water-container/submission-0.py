class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # brute force checks area for all index pairs and returns max

        # sorting jumbles indices, which is a problem for width

        best = 0

        L = 0
        R = len(heights) - 1

        while L < R:
            
            best = max(best, (R-L) * min(heights[L], heights[R]))

            if heights[L] >= heights[R]:
                R -= 1
            
            else:
                L += 1
        
        return best
