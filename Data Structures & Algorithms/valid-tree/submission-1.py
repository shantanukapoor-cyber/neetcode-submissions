
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Check connectivity — boolean semiring, flood from node 0
        visited = set()

        def dfs(node):
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(child)

        dfs(0)
        return len(visited) == n
            