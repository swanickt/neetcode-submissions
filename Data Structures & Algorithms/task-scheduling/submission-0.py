# We always want to run the task that still has the most remaining occurrences,
# because those are the hardest to fit into the schedule
# (they need more slots with cooldown gaps).

# So we:
#   - Keep a max-heap of tasks by their remaining count (most frequent on top).
#   - At each time unit, we take the most frequent available task and run it.
#   - After running a task, it goes into a cooldown queue with the time when it will be available again (current time + n).  
#   - When a task’s cooldown finishes, we push it back into the heap so it can be scheduled again.
#   - If the heap is empty but some tasks are still in cooldown, we can jump the current time forward to the next time when a task becomes available.

# This way we always use the CPU as efficiently as possible while respecting the cooldown.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-count for count in count.values()]
        heapq.heapify(maxHeap)

        # Note on the above. We don't actually care about the letters. Just the counts of each, because the cooldown is the same per letter.

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]

            else:
                count = 1 + heapq.heappop(maxHeap) # The second term is negative
                if count: # i.e., if not 0
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            
