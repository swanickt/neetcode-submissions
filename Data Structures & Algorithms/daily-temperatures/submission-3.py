class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                resolved_index = stack.pop()
                result[resolved_index] = i - resolved_index
            
            stack.append(i)
        
        return result


