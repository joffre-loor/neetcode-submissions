class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        tab = [0] * len(nums)

        tab[0] = nums[0]
        tab[1] = max(nums[1],nums[0])

        for i in range(2, len(nums)):
            tab[i] = max(tab[i-1], nums[i] + tab[i-2])

        return tab[-1]