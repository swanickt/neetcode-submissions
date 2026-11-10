class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # brute force:
        #   Compute all distances: O(n), sort by distances: O(nlogn),
        #   return k closest: O(k). Total: O(nlogn)
        #
        #   Compute all distances: O(n), create a min heap by distances: O(n),
        #   Pop k elements: O(klogn). Total: O(n + klogn(n))

        # ======= Total RT: O(n + klogn(n)), with Mem: O(n) =======
        
        """
        heap = [(points[i][0]**2 + points[i][1]**2, i) for i in range(len(points))]

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            index = heapq.heappop(heap)[1]
            res.append([points[index][0], points[index][1]])

        return res
        """

        # ======= Total RT: O(nlogn(k)), with Mem: O(k) =======

        heap = []

        for i in range(k):
            point = points[i]
            dist = - (point[0]**2 + point[1]**2)
            heapq.heappush(heap, (dist, i))


        for i in range(k, len(points)):
            point = points[i]
            dist = - (point[0]**2 + point[1]**2)

            if heap[0][0] < dist:
                heapq.heapreplace(heap, (dist, i))
        
        return [[points[x[1]][0], points[x[1]][1]] for x in heap]







        