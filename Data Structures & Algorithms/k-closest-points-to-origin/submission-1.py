class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)


        def calc_distance(x1, x2, y1, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        for point in points:
            dist = calc_distance(0, point[0], 0, point[1])
            heapq.heappush(min_heap, [-dist, point[0], point[1]])
            while len(min_heap) > k:
                heapq.heappop(min_heap)

        arr = []
        for triplet in min_heap:
            arr.append([triplet[1], triplet[2]])
        return arr
