class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for i in range(len(word)):
                char_count[ord(word[i]) - ord('a')] += 1

            map[str(char_count)].append(word)

        return list(map.values())
                