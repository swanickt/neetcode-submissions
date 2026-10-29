class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        # classic sliding window problem (fixed size)
        
        count = 0

        current_sum = 0

        for i in range(k):
            current_sum += arr[i]
        
        if (current_sum / k) >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            current_sum -= arr[i - k]
            current_sum += arr[i]

            if (current_sum / k) >= threshold:
                count += 1
        
        return count
        