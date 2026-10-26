class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max = 0
        for num in nums:
            if num == 1:
                curr += 1
                if curr > max:
                    max = curr
            else:
                curr = 0
        return max