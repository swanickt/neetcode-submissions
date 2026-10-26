class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for char in s:
            index = t.find(char) # returns index or -1 if missing
            if index == -1:
                return False
            t = t[:index] + t[index+1:len(t)]
        return True
