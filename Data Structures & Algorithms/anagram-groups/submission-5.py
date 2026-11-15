class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)

        for ana in strs:
            chars = [0] * 26
            for c in ana:
                chars[ord(c) - ord('a')] += 1
            
            groups[tuple(chars)].append(ana)

        
        return list(groups.values())