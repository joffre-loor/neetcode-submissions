class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        def distance(p1, p2):
            x_dist = (p1[0] - p2[0])**2
            y_dist = (p1[1] - p2[1])**2
            return math.sqrt(x_dist + y_dist)
        
        maxHeap = []
        for i in range(len(points)):
            dist = distance([0,0], points[i])

            if len(maxHeap) == k and maxHeap[0][0] < dist*-1:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-dist, points[i]))
            elif len(maxHeap) != k:
                heapq.heappush(maxHeap, (-dist, points[i]))
        
        res = []

        for dist, point in maxHeap:
            res.append(point)

        return res        

