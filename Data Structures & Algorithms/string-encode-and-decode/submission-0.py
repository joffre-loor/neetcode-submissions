class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + f"{len(string)}" + "#" + string
       
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
  
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            length = int(s[i : j])
            i = j + 1
            j = i + length
            string = s[i : j] 
            decoded.append(string)

            i = j 

        return decoded