class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort() # O(nlogn)

        i = 0
        while i < len(nums) - 2:
            
            diff = 0 - nums[i] # 2 sum target
            L = i + 1
            R = len(nums) - 1

            while L < R:
                
                two_sum = nums[L] + nums[R]

                if two_sum == diff:
                    
                    res.append([nums[i], nums[L], nums[R]])
                    
                    left_num = nums[L]
                    
                    while nums[L] == left_num and L < R:
                        L += 1
                
                elif two_sum < diff:
                    
                    left_num = nums[L]
                    
                    while nums[L] == left_num and L < R:
                        L += 1
                
                else:

                    right_num = nums[R]
                    
                    while nums[R] == right_num and L < R:
                        R -= 1
                    
                    
            
            num = nums[i]
            
            while nums[i] == num and i < len(nums) - 2:
                i+= 1
            
        return res


        # [-4,-1,-1,0,1,1,2]
