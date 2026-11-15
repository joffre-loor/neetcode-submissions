class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return 0
            
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))

            if grid[r][c] == 1:
                return 1 + dfs(r-1,c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)
            
            return 0
        

        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                maxArea = max(maxArea, dfs(i,j))

        return maxArea