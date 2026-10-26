class Solution:
    def findMin(self, nums: List[int]) -> int:   
        # Consider the array [3, 4, 1, 2]. Here, the array is rotated twice, 
        # resulting in two sorted segments: [3, 4] and [1, 2].
        #
        # The minimum element will be the first element of the right segment.
        # We can do a binary search to find this cut. 


        nums_length = len(nums)

        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound < upper_bound:  
            m = (lower_bound + upper_bound) // 2

            if nums[m] < nums[upper_bound]:
                upper_bound = m
            else:
                lower_bound = m + 1


        return nums[lower_bound]
