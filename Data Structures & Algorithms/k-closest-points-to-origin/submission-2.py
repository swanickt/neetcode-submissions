class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = [(x[0]**2 + x[1]**2, x) for x in points]

        return [x[1] for x in heapq.nsmallest(k, distances)]