class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.PQ = nums
        heapq.heapify(self.PQ)
        while len(self.PQ) > self.kth:
            heapq.heappop(self.PQ)

    def add(self, val: int) -> int:
        heapq.heappush(self.PQ, val)
        while len(self.PQ) > self.kth:
            heapq.heappop(self.PQ)
        return self.PQ[0]
            
