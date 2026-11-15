class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []
        def dfs(numClosed, numOpen):
            if numClosed == n == numOpen:
                add = ""
                for char in stack:
                    add += char
                res.append(add)
                return

            if numOpen < n:
                stack.append('(')
                dfs(numClosed, numOpen+1)
                stack.pop()
            
            if numClosed < numOpen:
                stack.append(')')
                dfs(numClosed+1, numOpen)
                stack.pop()
                
        
        dfs(0, 0)

        return res