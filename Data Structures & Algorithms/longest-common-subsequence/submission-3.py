class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # for the longest common subsequence.
        # f(i, j) = length of common subsequence at i in string 1 and j in string 2.
        # f(i, j) = text1[i] == text2[j] and there exist k < i 
        # and there exist l < j where text1[k] == text2[l]
        # f(i, j) = 1 + f(i-1, j-1) if text1[i] == text2[j]
        # f(i, j) = max(f(i-1,j), f(i,j-1)) if text1[i] != text2[j]
        # f(0, 0) = 0 or 1
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]

        