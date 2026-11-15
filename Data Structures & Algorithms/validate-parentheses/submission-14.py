class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = None
        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                if stack and stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack and stack[-1] == '{'  and char == '}':
                    stack.pop()
                elif stack and stack[-1] == '('  and char == ')':
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False

        return True

