class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Sliding window, implemented with a hash set (dictionary) for O(1) look up
        # Should allow for O(n) total worst case RT

        window = set()
        L = 0 # left pointer (lower bound of the window)

        for R in range(len(nums)): 
        # right pointer (window upper bound)
            
            if R - L > k:
                
                window.remove(nums[L])
                L += 1
            
            
            if nums[R] in window:
                return True
            
            else:
                window.add(nums[R])
            
        return False
            
            
