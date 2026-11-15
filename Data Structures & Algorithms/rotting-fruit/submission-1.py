class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh+=1

        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            
            if (r,c) in visited or grid[r][c] != 1:
                return False
            
            grid[r][c] = 2
            visited.add((r,c))
            q.append((r,c))
            return True
        

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                if addCell(r+1, c):
                    fresh-=1
                if addCell(r-1, c):
                    fresh-=1
                if addCell(r, c+1):
                    fresh-=1
                if addCell(r, c-1):
                    fresh-=1
            minutes+=1
        
        return minutes if fresh == 0 else -1



