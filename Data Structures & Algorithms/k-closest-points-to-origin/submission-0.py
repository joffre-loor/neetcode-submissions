class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)
        point_dict = {}

        def calc_distance(x1, x2, y1, y2):
            return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

        for point in points:
            dist = calc_distance(0, point[0], 0, point[1])
            if dist not in point_dict:
                point_dict[dist] = []
            point_dict[dist].append(point)
            heapq.heappush(min_heap, -dist)
            while len(min_heap) > k:
                popped_dist = -heapq.heappop(min_heap)
                if len(point_dict[popped_dist]) == 1:
                    del(point_dict[popped_dist])
                else:
                    del(point_dict[popped_dist][0])

        arr = []
        for item_list in list(point_dict.values()):
            for point in item_list:
             arr.append(point)
        return arr
