class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)

        for u,v,t in times:
            edges[u].append((v, t))

        q = [(0, k)]
        visited = set()
        t = 0
        while q:
            ti, ui = heapq.heappop(q)

            if ui in visited:
                continue
            
            visited.add(ui)
            t = ti
            for v, time in edges[ui]:
                
                if v not in visited:
                    heapq.heappush(q, (ti+time, v))

        return t if len(visited) == n else -1
            
