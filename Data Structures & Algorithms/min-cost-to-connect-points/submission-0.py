class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(len(points)):
                if i != j:
                    xj, yj = points[j]
                    dist = abs(xi-xj) + abs(yi-yj)
                    edges[i].append([dist, j])
                    edges[j].append([dist, i])
        
        pq = [[0,0]]
        res = 0
        visited = set()
        while pq:
            d, u = heapq.heappop(pq)

            if u in visited:
                continue
            
            res += d
            visited.add(u)

            for distance, vert in edges[u]:
                if vert not in visited:
                    heapq.heappush(pq, [distance, vert])
        
        return res