class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        numComponents = 0
        def dfs(node):
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                numComponents+=1
        

        return numComponents



