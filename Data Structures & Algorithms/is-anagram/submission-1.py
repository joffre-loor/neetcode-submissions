class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashCount = defaultdict(int)
        for i, char in enumerate(s):
            hashCount[ord(s[i]) - ord('a')] += 1
            hashCount[ord(t[i]) - ord('a')] -= 1
        
        for val in hashCount.values():
            if val != 0:
                return False
        
        return True