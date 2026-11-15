class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operands = set(["*", "-", "+", "/"])
        for token in tokens:
            print(stack)
            if token in operands:
                second = int(stack.pop())
                first = int(stack.pop())
            else:
                stack.append(token)
                continue
            if token == "+":
                add = first + second
                stack.append(add)
            elif token == "-":
                subtract = first - second
                print(subtract)
                stack.append(subtract)
            elif token == "*":
                mult = first * second
                stack.append(mult)
            elif token == "/":
                mult = int(first / second)
                stack.append(mult)
        
        return int(stack[0])