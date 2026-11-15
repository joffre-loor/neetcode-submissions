class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for anagram in strs:
            count = [0] * 26
            for c in anagram:
                count[ord(c) - ord('a')] += 1 
            group[tuple(count)].append(anagram)
        
        return list(group.values())
            