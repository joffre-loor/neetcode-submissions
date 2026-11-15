class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
        
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            
            if len(adj[curr]) == 0:
                return True
            visited.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visited.remove(curr)
            adj[curr] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True