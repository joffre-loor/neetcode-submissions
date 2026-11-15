class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = ""

        l = 0
        minS = 201
        for s in strs:
            minS = min(len(s), minS)
        
        currC = None
        while l < minS:
            for s in strs:
                if not currC:
                    currC = s[l]
                    continue
                
                if s[l] == currC:
                    continue
                else:
                    return common
            common += currC
            l+=1
            currC = None



        return "".join(common)