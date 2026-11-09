class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0
        R = 0

        longest = 0

        current_window_char_counts = defaultdict(int)

        while R < len(s):

            if current_window_char_counts[s[R]] > 0:
                while current_window_char_counts[s[R]] > 0:
                    current_window_char_counts[s[L]] -= 1
                    L += 1
            
            longest = max(longest, R - L + 1)

            current_window_char_counts[s[R]] += 1

            R += 1
        
        return longest

