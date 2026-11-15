class Solution:
    def totalNQueens(self, n: int) -> int:
        
        board = [["."] * n for _ in range(n)]
        posDiag = set()
        negDiag = set()
        col = set()


        count = 0
        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return


            for c in range(n):
                if (r+c) in posDiag or (r-c) in negDiag or c in col:
                    continue
                
                posDiag.add((r+c))
                negDiag.add((r-c))
                col.add(c)
                backtrack(r+1)

                posDiag.remove((r+c))
                negDiag.remove((r-c))
                col.remove(c)

        backtrack(0)
        return count