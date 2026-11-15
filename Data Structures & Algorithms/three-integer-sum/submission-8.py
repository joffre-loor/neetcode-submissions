class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                check = nums[l] + nums[r] + num
                if check > 0:
                    r-=1
                elif check < 0:
                    l+=1
                else:
                    triplets.append([nums[l], nums[r], num])
                    l+=1
                    r-=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
        return triplets