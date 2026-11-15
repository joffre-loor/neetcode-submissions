class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        pq = []

        counts = Counter(tasks)
        for val in counts.values():
            heapq.heappush(pq, -val)

        time = 0
        q = deque()

        while pq or q:
            time+=1

            if not pq:
                time = q[0][1]
            else:
                process = 1 + heapq.heappop(pq)
                if process:
                    q.append([process, time+n])
            if q and q[0][1] == time:
                heapq.heappush(pq, q.popleft()[0])
        return time