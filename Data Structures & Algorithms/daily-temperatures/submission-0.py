class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results = []

        # some kind of monotonic stack where we loop from temp[n-1] to temp[0]

        # brute force is O(n**2)

        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            # at this point, either stack is empty (set result to 0)
            # or, stack[-1] > temperatures[i], so we set results to day_count
            # Either way, we then push current day to the stack

            if not stack:
                results.append(0)
            else:
                warmer_day_index = stack[-1][1] # DO NOT REMOVE WARMER DAY!
                results.append(warmer_day_index - i)

            stack.append((temperatures[i], i))
    
        results.reverse()

        return results

