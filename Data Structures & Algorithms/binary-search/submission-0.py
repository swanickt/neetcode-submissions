class Solution:

    def index_binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        

        if left == right:
            
            if nums[left] == target:
                return left
            else:
                return -1
        
        else: # i.e., left < right
            
            m = (left + right) // 2

            
            if target <= nums[m]:
                return self.index_binary_search(nums, left, m, target)
            
            else:
                return self.index_binary_search(nums, m + 1, right, target)

    def search(self, nums: List[int], target: int) -> int:

        return self.index_binary_search(nums, 0, len(nums) - 1, target)

        