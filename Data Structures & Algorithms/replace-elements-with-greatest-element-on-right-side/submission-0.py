class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curr_max = arr[-1]
        arr[-1] = -1
        i = len(arr) - 2

        while i >= 0:
            curr = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, curr)

            i -= 1
        
        return arr