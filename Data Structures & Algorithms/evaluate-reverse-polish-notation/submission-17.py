class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operands = set(["*", "-", "+", "/"])
        for token in tokens:
            print(stack)
            if token in operands:
                second = stack.pop()
                first = stack.pop()
            else:
                stack.append(int(token))
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
        
        return stack[0]