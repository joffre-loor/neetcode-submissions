class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for digit in digits:
            string += str(digit)
        
        num = int(string) + 1
        string = str(num)
        plus = []
        for char in string:
            plus.append(char)
        
        return plus