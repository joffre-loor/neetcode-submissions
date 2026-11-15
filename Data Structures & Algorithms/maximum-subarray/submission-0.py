class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()

        for i in range(1, len(nums)):
            dp[i] = max(dp[i], nums[i] + dp[i-1])
        
        return max(dp)