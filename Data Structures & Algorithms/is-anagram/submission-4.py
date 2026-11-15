class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 0
            if t[i] not in hashmap:
                hashmap[t[i]] = 0
            hashmap[s[i]] += 1
            hashmap[t[i]] -=1
        
        for item in hashmap.values():
            if item !=0:
                return False
        return True