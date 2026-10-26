class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums

        initial_len = len(ans)
        for i in range(initial_len):
            ans.append(ans[i])
        
        return ans