class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = None
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                check = stack.pop()
                if check == '(' and bracket == ')':
                    continue
                elif check == '{' and bracket == '}':
                    continue
                elif check == '[' and bracket == ']':
                    continue
                else:
                    return False

        if len(stack) > 0:
            return False
        return True

