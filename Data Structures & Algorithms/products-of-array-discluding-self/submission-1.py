class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        for num in nums:
            if num != 0:
                product = product * num
            if num == 0:
                zeroes +=1
            if zeroes == 2:
                return [0] * len(nums)

        arr = []
        for num in nums:
            if zeroes == 1:
                if num == 0:
                    arr.append(product)
                else:
                    arr.append(0)
            else:
                arr.append(product // num)            
        return arr