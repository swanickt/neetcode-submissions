class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                curr_count += 1
            else:
                nums[i - curr_count] = nums[i]
                k += 1
        return k