class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # keep a min heap of length k
        # loop through all elements kick out the smallest if new element is larger

        # at the end, left with the k largest elements. The min of these
        # (i.e., smallest element in the heap) is the kth largest.

        heap = nums[:k]

        heapq.heapify(heap)

        for i in range(k, len(nums)):

            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        
        return heap[0]

        # O(nlog(k))