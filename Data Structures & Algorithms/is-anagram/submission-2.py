class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same number of characters
        if len(s) != len(t):
            return False

        # Initialize a frequency array for the 26 lowercase English letters
        # Each index corresponds to a letter: 0 = 'a', 1 = 'b', ..., 25 = 'z'
        count = [0] * 26

        # Count character occurrences in both strings
        for i in range(len(s)):
            # Increment the count for the current character in s
            # ord(char) returns its Unicode value; subtracting ord('a')
            # maps lowercase letters to indices 0–25
            count[ord(s[i]) - ord('a')] += 1

            # Decrement the count for the current character in t
            count[ord(t[i]) - ord('a')] -= 1

        # If the strings are anagrams, every character's net count is zero
        for val in count:
            if val != 0:
                return False  # A character appears a different number of times

        return True  # All character frequencies match
