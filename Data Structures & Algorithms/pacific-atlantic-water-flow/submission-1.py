class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            visited.add((r,c))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                    dfs(nr, nc, visited)
        for i in range(m):
            dfs(i, 0, pacific)  
            dfs(i, n-1, atlantic)  
        for i in range(n):
            dfs(0, i, pacific) 
            dfs(m-1, i, atlantic)            
        
        return list(pacific.intersection(atlantic))
                    