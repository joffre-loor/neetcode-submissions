class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0
        for num in nums:
            bit = bit ^ num
        return bit