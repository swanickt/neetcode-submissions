class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        heap = []

        for num in counts.keys():
            
            heapq.heappush(heap, (counts[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [x[1] for x in heap]

                    
        
        