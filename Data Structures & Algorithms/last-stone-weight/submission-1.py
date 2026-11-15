class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 0:
            if len(max_heap) == 1:
                break
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            if stone1 > stone2:
                heapq.heappush(max_heap, -(stone1-stone2))
            elif stone2 > stone1: 
                heapq.heappush(max_heap, -(stone2-stone1))
        return -max_heap[0] if len(max_heap)==1 else 0