class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets=[]
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            
            l, r = i+1, len(nums)-1

            while l < r:
                trip_sum = nums[l] + nums[r] + num
                if trip_sum < 0:
                    l+=1
                elif trip_sum > 0:
                    r-=1
                else:
                    triplets.append([nums[l], nums[r], num])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        
        return triplets