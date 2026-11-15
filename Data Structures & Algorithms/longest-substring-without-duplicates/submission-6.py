class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0

        count = defaultdict(int)
        
        maxSubstring = 0

        while r < len(s):
            if r - l > maxSubstring:
                maxSubstring = r - l
            while count[s[r]] == 1:
                count[s[l]] -=1
                l+=1

            count[s[r]] += 1
            r+=1

        if r - l > maxSubstring:
                maxSubstring = r - l
        return maxSubstring