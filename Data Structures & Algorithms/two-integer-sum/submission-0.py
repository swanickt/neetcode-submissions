class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in map:
                return [min(i, map[j]), max(i, map[j])]
            map[nums[i]] = i