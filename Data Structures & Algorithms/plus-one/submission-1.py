class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = ""
        for d in digits:
            num += str(d)

        num = str(int(num)+1)

        res = []
        for d in num:
            res.append(int(d))

        return res