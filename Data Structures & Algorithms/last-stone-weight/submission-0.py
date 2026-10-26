class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if abs(x) > abs(y):
                y = -(abs(x) - abs(y))
                heapq.heappush(heap, y)
        
        if len(heap) > 0:
            return -heap[0]
        return 0
        
