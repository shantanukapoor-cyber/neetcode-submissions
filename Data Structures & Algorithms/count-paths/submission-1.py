class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # can move down or right.
        # so reachable paths = 1 + right reachable + 1 + down reachable.
        # f(r, c) = ways to reach (r, c)
        # r, c should be 0 <= r < m and 0 <= c < n
        # f(r, c) = f(r-1, c) + f(r, c-1)
        # f(0, c) = 1
        # f(r, 0) = 1
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]