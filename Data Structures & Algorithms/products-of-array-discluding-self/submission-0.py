class Solution: 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        prefix_prod = 1
        for i in range(len(nums)):
            output.append(prefix_prod)
            prefix_prod *= nums[i]
        
        suffix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return output




