class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary mapping character-frequency patterns to lists of anagrams.
        # defaultdict(list) automatically creates an empty list for new keys.
        res = defaultdict(list)

        # Process each string in the input list.
        for s in strs:
            # Initialize a frequency array for the 26 lowercase English letters.
            # Each index corresponds to a letter: 0 = 'a', 1 = 'b', ..., 25 = 'z'.
            count = [0] * 26

            # Count the occurrences of each character in the current string.
            for c in s:
                # ord(c) - ord('a') maps lowercase letters to indices 0–25.
                count[ord(c) - ord('a')] += 1

            # Convert the frequency array to a tuple so it can be used
            # as a dictionary key (lists are mutable and unhashable).
            # Anagrams have identical character frequencies, so they
            # produce the same tuple and are grouped together.
            res[tuple(count)].append(s)

        # Return all groups of anagrams as a list of lists.
        return list(res.values())
                