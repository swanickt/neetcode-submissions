class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # set of seen numbers

        for num in nums:
            if num in seen:
                return True # If num previously seen, return true
            seen.add(num) # Add to set of seen nums
            
        return False # no nums seen more than once