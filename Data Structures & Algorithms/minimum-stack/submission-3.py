class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minS:
            if val < self.minS[-1]:
                self.minS.append(val)
            else:
                self.minS.append(self.minS[-1])
        else:
            self.minS.append(val)
        
        print(self.minS)

    def pop(self) -> None:
        self.minS.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.minS)
        return self.minS[-1]
