class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l, r = 0, 0
        while r < len(nums):
            while q and q[0] < l:
                q.popleft()

            while q and nums[r] >= nums[q[0]]:
                q.popleft()
            
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
                
            q.append(r)
            if r < k-1:
                r+=1
            else:
                res.append(nums[q[0]])
                l+=1
                r+=1
            print("current q: ", q)

        return res