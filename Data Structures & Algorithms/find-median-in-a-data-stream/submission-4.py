class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.large) <= len(self.small):
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num*-1)
        
        if self.large and self.small and self.small[0]*-1 > self.large[0]:
            sm = heapq.heappop(self.small)*-1
            lg = heapq.heappop(self.large)
            heapq.heappush(self.small, lg*-1)
            heapq.heappush(self.large, sm)
        print(f"{self.small} . . . {self.large}")


    def findMedian(self) -> float:
        if self.large and not self.small:
            return self.large[0]
        
        if not self.large and self.small:
            return self.small[0]
        
        total = len(self.small) + len(self.large)

        if total % 2 == 0:
            return ((self.small[0]*-1) + self.large[0]) / 2
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return self.small[0]*-1
        
        