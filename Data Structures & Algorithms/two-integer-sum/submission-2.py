class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_num_to_index_map = {}

        for i, num in enumerate(nums):
            
            diff = target - num
           
            if diff in seen_num_to_index_map:
                return [min(i, seen_num_to_index_map[diff]), 
                max(i, seen_num_to_index_map[diff])]

            seen_num_to_index_map[num] = i