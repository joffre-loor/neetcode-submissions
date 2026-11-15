class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        check = {}
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
            check[char] = 0
        
        def compare(original, check):
            for char in t:
                if original[char] > check[char]:
                    return False
            
            return True

        l, r = 0, 0
        minL, minR = 0, 0
        minStr = len(s)+1
        while r < len(s):
            if s[r] in check:
                check[s[r]]+=1

            while compare(hashmap, check):
                if r-l+1 < minStr:
                    minStr = r-l+1
                    minL = l
                    minR = r
                if s[l] in check:
                    check[s[l]] -= 1
                l+=1
                while l < r and s[l] not in check:
                    l+=1
        
            r+=1

        return "" if minStr > len(s) else s[minL:minR+1]