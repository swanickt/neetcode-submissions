import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # brute force: 
        #   can create frequency map O(n), sort by frequency O(nlogn),
        #   output top k O(k). Total: O(nlogn)
        #
        # Or:
        #   can create frequency map O(n), heapify (max) by frequency O(n),
        #   pop and return k elements O(klogn). Total: O(n + klogn)

        counts = Counter(nums) # map of elements to counts

        heap = [(-counts[c], c) for c in counts.keys()]

        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res






