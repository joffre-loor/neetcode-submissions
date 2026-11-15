class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        arr = [0] * len(temperatures)
        index = 0
        while index < len(temperatures):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                popped = stack.pop()
                arr[popped] = index - popped
            stack.append(index)
            index += 1

        while len(arr) < len(temperatures):
            arr.append(0)

        return arr