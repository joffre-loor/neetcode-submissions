class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        one, two = 0, 0
        three, four = 0,0

        for i in range(len(nums)-1):
            temp = max(one + nums[i], two)
            one = two
            two = temp

        for i in range(1, len(nums)):
            temp = max(three + nums[i], four)
            three = four
            four = temp

        return max(two, four)