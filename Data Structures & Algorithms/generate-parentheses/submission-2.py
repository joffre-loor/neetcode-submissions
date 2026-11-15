class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(curr, numOpen, numClosed):
            if numOpen == numClosed and numClosed == n:
                res.append(curr)
                return
            
            if numClosed < numOpen:
                backtrack(curr+")", numOpen, numClosed+1)
            
            if numOpen < n:
                backtrack(curr+"(", numOpen+1, numClosed)

        
        backtrack("", 0, 0)
        return res