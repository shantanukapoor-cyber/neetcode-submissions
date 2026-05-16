class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        def spread(row, column):
            if grid[row][column] == 0:
                return 0
            grid[row][column] = 0
            area = 1                                        # count myself
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = row + dr, column + dc
                if 0 <= nr < m and 0 <= nc < n:
                    area += spread(nr, nc)                  # add what children found
            return area                                     # send total UP

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, spread(i, j))

        return max_area