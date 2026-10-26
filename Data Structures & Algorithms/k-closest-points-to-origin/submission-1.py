class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = [(math.sqrt(x[0]**2 + x[1]**2), x) for x in points]
        heapq.heapify(heap)

        k_closest = []

        for _ in range(k):
            k_closest.append(heapq.heappop(heap)[1])
        
        return k_closest