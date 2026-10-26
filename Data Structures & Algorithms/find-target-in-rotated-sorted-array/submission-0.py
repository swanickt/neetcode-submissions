class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        upper_bound = len(nums) - 1
        lower_bound = 0

        while lower_bound <= upper_bound:

            m = (lower_bound + upper_bound) // 2

            if nums[m] == target:
                return m
            
            if nums[lower_bound] <= nums[m]:
                if target > nums[m] or target < nums[lower_bound]:
                    lower_bound = m + 1
                else:
                    upper_bound = m - 1
            
            else:
                if target < nums[m] or target > nums[upper_bound]:
                    upper_bound = m -1 
                else:
                    lower_bound = m + 1

        return -1
