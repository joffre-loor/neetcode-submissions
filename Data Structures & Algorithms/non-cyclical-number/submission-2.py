class Solution:
    def isHappy(self, n: int) -> bool:
        

        num = n
        visited = set()
        while num != 1:
            total = 0
            if num in visited:
                return False
            
            visited.add(num)

            for digit in str(num):
                total += int(digit)**2
            
            print(total)
            num = total

        return True
