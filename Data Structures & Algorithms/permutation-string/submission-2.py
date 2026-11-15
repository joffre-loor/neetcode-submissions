class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        s1Map = {}
        s2Map = {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1
        for char in s2:
            s2Map[char] = s2Map.get(char, 0)

        while r < len(s2):
            if r - l + 1 > len(s1):
                s2Map[s2[l]] -= 1
                l+=1
            s2Map[s2[r]] += 1

            check = True
            for char, value in s1Map.items():
                if char not in s2Map:
                    return False
                if s1Map[char] != s2Map[char]:
                    check = False
            
            if check:
                return True
            
            r+=1
        
        return False