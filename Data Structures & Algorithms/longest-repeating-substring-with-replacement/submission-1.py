class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0

        charMax = 0
        charMap = {}
        string = 0
        while r < len(s):
            if s[r] not in charMap:
                charMap[s[r]] = 0
            
            charMap[s[r]] += 1
            charMax = max(charMax, charMap[s[r]])
            
            if r - l + 1 > charMax + k:
                charMap[s[l]] -= 1
                l+=1
            
            string = max(string, r -l + 1)
            r+=1
        
        return string
