class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        
        count = defaultdict(int)
        freq = 0
        longest = 0
        while r < len(s):
            count[s[r]] += 1
            freq = max(freq, count[s[r]])

            while (r-l+1) - freq > k:
                count[s[l]]-=1
                l+=1
            
            longest = max(longest, r-l+1)
            r+=1
        
        return longest

                
            
            