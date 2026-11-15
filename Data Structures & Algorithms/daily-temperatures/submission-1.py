class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(i)
                continue
            
            while len(stack) != 0:
                index = stack.pop()
                if temperatures[index] < temp:
                    res[index] = i-index
                else:
                    stack.append(index)
                    break
            stack.append(i)
                
        print(stack)
        return res
            
