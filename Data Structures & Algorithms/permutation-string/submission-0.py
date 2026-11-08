class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        s1_signature = [0] * 26
        
        for char in s1:
            s1_signature[ord(char) - ord('a')] += 1
        
        s2_signature = [0] * 26

        for i in range(len(s1)):
            s2_signature[ord(s2[i]) - ord('a')] += 1

        if s2_signature == s1_signature:
            return True
        
        k = len(s1)

        for i in range(k, len(s2)):
            s2_signature[ord(s2[i-k]) - ord('a')] -= 1
            s2_signature[ord(s2[i]) - ord('a')] += 1
            
            if s2_signature == s1_signature:
                return True
        
        return False