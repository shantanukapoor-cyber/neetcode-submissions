class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        connected_components = 0

        def dfs(node):
            visited.add(node)
            for child in adj_list[node]:
                if child not in visited:
                    dfs(child)
        
        for vertex in adj_list:
            if vertex not in visited:
                dfs(vertex)
                connected_components += 1
        for i in range(n):
            if i not in visited:
                connected_components += 1
        return connected_components