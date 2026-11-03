class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L = 0
        R = len(s) - 1

        while L < R:
            # If we find a palindrome contradiction, return False

            if not s[L].isalnum():
                L += 1
            
            elif not s[R].isalnum():
                R -= 1
            
            # otherwise, both characters are alphanumeric
            elif s[L].lower() != s[R].lower():
                return False
            
            else:
                L += 1
                R -= 1
        
        return True