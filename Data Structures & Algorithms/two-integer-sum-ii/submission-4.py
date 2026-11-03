class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # find solution indices and add 1 to each before returning

        L = 0
        R = len(numbers) - 1

        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L+1, R+1]
            
            elif total < target:
                L += 1
            
            else:
                R -= 1
        
        # assuming loop body is correct, always having exactly one solution should mean we never reach here