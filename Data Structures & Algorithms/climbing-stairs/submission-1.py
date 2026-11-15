class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        one, two = 1, 2

        for i in range(2, n):
            temp = one + two
            one = two
            two = temp
        
        return two