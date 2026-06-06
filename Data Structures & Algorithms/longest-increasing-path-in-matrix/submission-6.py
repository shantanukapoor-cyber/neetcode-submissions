from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # valid moves -> [(0,1),(0,-1),(1,0),(-1,0)]
        # f(i, j) = strictly increasing length legal possible from here.
        # f(i, j) = 1 + max(valid(f(i, j+1), f(i, j-1), f(i+1, j). f(i-1, j))
        # where next move is strictly greater than current move.
        sys.setrecursionlimit(10**6)
        m = len(matrix) 
        # m = 2, n = 1
        n = len(matrix[0])
        @cache
        def longestPath(i, j):
            max_ways = 0
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[i][j]:
                    max_ways = max(max_ways, longestPath(nr, nc))
            return 1 + max_ways
        global_max = float('-inf')
        for i in range(m):
            for j in range(n):
                position_max = longestPath(i, j)
                global_max = max(global_max, position_max)
        return global_max