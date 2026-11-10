import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones_heap = [-stone for stone in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            
            x = -heapq.heappop(stones_heap)
            y = -heapq.heappop(stones_heap)

            if x > y:
                heapq.heappush(stones_heap, -(x-y))


        return -stones_heap[0] if stones_heap else 0
