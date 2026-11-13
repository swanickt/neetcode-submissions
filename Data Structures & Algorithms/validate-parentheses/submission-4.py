class Solution:
    def isValid(self, s: str) -> bool:
        
        closed_to_open = {')': '(', ']': '[', '}': '{'}
        
        stack = []
        for char in s:
            if char in closed_to_open:           
                if not stack or stack.pop() != closed_to_open[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack
            
            

