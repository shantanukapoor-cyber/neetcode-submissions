class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        m, n = len(grid), len(grid[0])
        def spread(row, column):
            if grid[row][column] == "0":
                return
            grid[row][column] = "0"
            for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, column + dc
                if 0 <= nr < m and 0 <= nc < n :
                    spread(nr, nc)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    spread(i, j)
        return island_count