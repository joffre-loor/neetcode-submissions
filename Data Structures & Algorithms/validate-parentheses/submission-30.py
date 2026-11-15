class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack or c == ')' and stack[-1] != '(' or c == ']' and stack[-1] != '[' or c == '}' and stack[-1] != '{':
                return False
            elif len(stack) > 0:
                stack.pop()
        
        if stack:
            return False
            
        return True