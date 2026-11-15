class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num != 1:
            int_s = str(num)
            sqrs = 0
            for char in int_s:
                sqrs += int(char) ** 2
            
            if sqrs in seen:
                return False
            
            seen.add(sqrs)
            num = sqrs

        return True