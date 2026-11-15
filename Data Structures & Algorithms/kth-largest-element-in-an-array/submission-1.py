class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            print(pq)
            if len(pq) == k and num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)
            elif len(pq) != k:
                heapq.heappush(pq, num)
        

        return pq[0]