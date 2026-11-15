class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    grid[r][c] = 1
                else:
                    top = grid[r-1][c] if r > 0 else 0
                    left = grid[r][c-1] if c > 0 else 0
                    grid[r][c] = top + left
                    
        return grid[m-1][n-1]
        