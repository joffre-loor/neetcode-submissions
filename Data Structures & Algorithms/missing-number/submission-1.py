class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = len(nums)
        for i in range(0, check):
            check ^= nums[i] ^ i

        return check