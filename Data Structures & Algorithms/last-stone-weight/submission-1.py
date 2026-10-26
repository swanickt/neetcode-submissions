class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heapify creates a min heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            
            heaviest = - heapq.heappop(heap)
            second_heaviest = - heapq.heappop(heap)

            if second_heaviest < heaviest:
                heapq.heappush(heap, - (heaviest - second_heaviest))
        

        # At this point, heap has 1 or 0 stones

        if len(heap) == 0:
            return 0
        
        return - heap[0]