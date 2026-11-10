import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        heap = [-count for count in counts.values()]

        heapq.heapify(heap)

        q = deque()

        t = 0
       
        while heap or q:
            
            if q and q[0][0] <= t:
                item = q.popleft()
                heapq.heappush(heap, (item[1]))
            
            if heap:
                item = heapq.heappop(heap)
                if item < -1:
                    q.append((t+n+1, item + 1))

            t += 1

        return t
