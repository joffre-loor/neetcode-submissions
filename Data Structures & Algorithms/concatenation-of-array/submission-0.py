class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        new = nums.copy()

        for num in nums:
            new.append(num)

        return new