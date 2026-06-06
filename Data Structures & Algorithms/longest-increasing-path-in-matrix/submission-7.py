from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # List of all cells with their coordinates and value
        cells = [(matrix[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort(reverse=True)  # descending by value
        
        dp = [[1] * n for _ in range(m)]
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for val, i, j in cells:
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > val:
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
        
        return max(max(row) for row in dp)