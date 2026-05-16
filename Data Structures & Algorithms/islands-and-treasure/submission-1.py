class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # since we need to get nearest from treasure.
        from collections import deque
        m, n = len(grid), len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[row][col] + 1
                        queue.append((nr, nc))


            
            