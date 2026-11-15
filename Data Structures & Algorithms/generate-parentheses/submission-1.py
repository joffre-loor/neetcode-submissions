class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dfs(numOpen, numClosed):
            if numOpen == numClosed == n:
                toAdd = ""
                for char in stack:
                    toAdd += char
                res.append(toAdd)
                return
            
            if numOpen < n:
                stack.append("(")
                dfs(numOpen+1,numClosed)
                stack.pop()
            
            if numClosed < numOpen:
                stack.append(")")
                dfs(numOpen, numClosed+1)
                stack.pop()
        
        dfs(0, 0)

        return res