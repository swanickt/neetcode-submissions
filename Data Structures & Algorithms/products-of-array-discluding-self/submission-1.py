class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix_product = [1] * len(nums)
        suffix_product = [1] * len(nums)

        for i in range(1, len(nums)): # i:1,..,n-1

            n = len(nums)

            prefix_product[i] = prefix_product[i-1] * nums[i-1]

            suffix_product[n-1-i] = suffix_product[n-1-i + 1] * nums[n-1-i + 1]
        
        output = []

        for i in range(len(nums)):
            output.append(prefix_product[i] * suffix_product[i])
        
        return output
        