class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # brute force:
        #   Compute all distances: O(n), sort by distances: O(nlogn),
        #   return k closest: O(k). Total: O(nlogn)
        #
        #   Compute all distances: O(n), create a min heap by distances: O(n),
        #   Pop k elements: O(klogn). Total: O(n + klogn(n))

        heap = [(points[i][0]**2 + points[i][1]**2, i) for i in range(len(points))]

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            index = heapq.heappop(heap)[1]
            res.append([points[index][0], points[index][1]])

        return res
        