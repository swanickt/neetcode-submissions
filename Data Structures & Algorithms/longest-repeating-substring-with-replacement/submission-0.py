class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        most_common_window_char = s[0]

        counts = {s[0]: 1}

        L = 0
        R = 1

        best = 1
        
        while R < len(s):
            counts[s[R]] = counts.get(s[R], 0) + 1
            
            if counts[s[R]] > counts[most_common_window_char]:
                most_common_window_char = s[R]
            
            while sum(counts[c] for c in counts.keys()) - counts[most_common_window_char] > k:
                counts[s[L]] -= 1
                L += 1

                for char in counts:
                    if counts[char] > counts[most_common_window_char]:
                        most_common_window_char = char
            
            best = max(best, R-L+1)

            R += 1
        
        return best



