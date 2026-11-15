class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(curr, numClosed, numOpen):
            if numClosed == n and numOpen == n:
                res.append(curr)
                return
            

            if numOpen > numClosed:
                backtrack(curr+")", numClosed+1, numOpen)
            
            if numOpen < n:
                backtrack(curr+"(", numClosed, numOpen+1)
        
        backtrack("", 0,0 )
        return res