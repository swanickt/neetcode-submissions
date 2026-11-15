import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Brute force is:
        #   make a counter of the elements in nums
        #   sort by frequency (descending order)
        #   return k most frequent

        # The above is O(nlogn) RT (for sorting) and O(W) space where W
        # is the number of distinct elemetns

        # can we do better with a heap? (i.e., no sorting)
        # Counter/frequency map creation is O(n)
        # Maintain a min heap of size K by min frequency, by iterating over
        # all elements in frequency map. At the end,
        # K largest frequency elements will be left. 

        # O(n + nlogk + k) = O(nlogk), sapce is O(W + k)

        counts = Counter(nums)

        heap = []

        for element, count in counts.items():
            
            if len(heap) < k:
                heapq.heappush(heap, (count, element))
            
            # else, len(heap) == k

            elif heap[0][0] < count:
                heapq.heapreplace(heap, (count, element))
        
        return [item[1] for item in heap]
            
