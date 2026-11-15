class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_string = bin(n)
        count = 0
        for char in bin_string:
            if char == '1':
                count+=1

        return count