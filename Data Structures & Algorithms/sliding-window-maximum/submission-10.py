class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        pq = []

        l, r = 0, 0
        pq = []
        while r < k:
            heapq.heappush(pq,(nums[r]*-1, r))
            r+=1

        res = []
        res.append(pq[0][0]*-1)
        while r < len(nums):
            l+=1
            if r < len(nums):
                heapq.heappush(pq, (nums[r]*-1, r))

            while pq and pq[0][1] < l:
                heapq.heappop(pq)
            
            res.append(pq[0][0]*-1)

            r+=1
            

        return res