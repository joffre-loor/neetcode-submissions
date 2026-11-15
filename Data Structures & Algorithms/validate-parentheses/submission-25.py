class Solution:
    def isValid(self, s: str) -> bool:
        openToClosed = {")":"(", ']':'[', '}':'{'}
        stack=[]
        for c in s:
            if c in openToClosed:
                if stack and stack[-1] == openToClosed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False

        return True