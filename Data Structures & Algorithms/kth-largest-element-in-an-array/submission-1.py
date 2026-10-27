class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Could heapify [-x for x in nums] to get a max heap
        # and return the kth popped element.
        
        # Heapify takes O(n) and each pop is O(logn), so worst case O(klogn)
        # But solution wants max O(nlogk) time and O(k) space. 
        # This heap approach requires O(n) space

        # O(k) space is a big hint of using a heap of k elements

        return heapq.nlargest(k, nums)[-1]

        # heapq.nlargest(k, nums) returns a list containing the k largest values
        # sorted from largest to smallest
        # Therefore, heapq.nlargest(k, nums)[-1] selects the last element of that list
