class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        m, n = len(grid), len(grid[0])
        def spread(row, column):
            if grid[row][column] == "0":
                return
            grid[row][column] = "0"
            if row > 0:
                spread(row - 1, column)
            if row < m - 1:
                spread(row + 1, column)
            if column > 0:
                spread(row, column - 1)
            if column < n - 1:
                spread(row, column + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_count += 1
                    spread(i, j)
        return island_count