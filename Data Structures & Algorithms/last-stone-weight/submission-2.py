class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap) * -1
            x = heapq.heappop(maxHeap) * -1
            print(f"x: {x}, y: {y}")
            diff = 0
            if x < y:
                y = y - x
                heapq.heappush(maxHeap, y * -1)
        
        print(maxHeap)
        return maxHeap[0] * -1 if len(maxHeap) == 1 else 0  

