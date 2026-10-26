class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [(math.sqrt(x[0]**2 + x[1]**2), x) for x in points]

        heapq.heapify(distances)

        out = []
        for i in range(k):
            out.append(heapq.heappop(distances)[1])
        
        return out
