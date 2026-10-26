class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # One approach is just sort and choose the (k-1) index element

        # Or heap
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for i in range(k-1):
            heapq.heappop(max_heap)
        
        return - heapq.heappop(max_heap)
