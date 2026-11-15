class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            if (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append((r,c))

        dist = 0
        while q:
            currLen = len(q)

            for i in range(currLen):
                r, c = q.popleft()
                
                grid[r][c] = dist
                addCell(r-1, c)
                addCell(r, c-1)
                addCell(r, c+1)
                addCell(r+1, c)
            dist+=1
