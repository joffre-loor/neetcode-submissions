class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        posDiag = set()
        negDiag = set()
        colSet = set()

        board = [["."]*n for _ in range(n)]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (r-c) in negDiag or (r+c) in posDiag or c in colSet:
                    continue
                
                colSet.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                board[r][c] = "Q"

                backtrack(r+1)

                colSet.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                board[r][c] = "."


        
        backtrack(0)
        return res