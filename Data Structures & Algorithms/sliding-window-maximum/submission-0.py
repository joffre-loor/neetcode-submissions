class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l, r = 0, k
        res=[]
        while r < len(nums)+1:
            maxNum = -1001
            for i in range(l, r):
                maxNum = max(maxNum, nums[i])
            
            l+=1
            r+=1
            res.append(maxNum)
        
        return res