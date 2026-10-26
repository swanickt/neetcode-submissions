class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            
            elif stack == []:
                return False

            elif char == ')':
                if stack.pop() != '(':
                    return False
            
            elif char == ']':
                if stack.pop() != '[':
                    return False
           
            elif char == '}':
                if stack.pop() != '{':
                    return False
            
        return stack == []