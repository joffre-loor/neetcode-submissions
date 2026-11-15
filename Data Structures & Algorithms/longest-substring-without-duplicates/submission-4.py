class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r  = 0, 0

        check = set()
        maxStr = 0
        while r < len(s):
            if s[r] in check:
                print(f"in here {s[r]}")
                while s[l] != s[r]:
                    print(f"left:{s[l]}, right:{s[r]}")
                    check.remove(s[l])
                    l+=1
                check.remove(s[l])
                l+=1

            check.add(s[r])
            r+=1
            maxStr = max(maxStr, len(check))
            
        return maxStr

            


            