class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # we are at i position in s and j position in t.
        # first condition it can either match or not match.
        # if it matches, we either select the first occurence current 
        # or skip and go to next.
        # if it doesn't match we can only skip.
        # f(i, j) = f(i+1, j) + f(i+1, j+1) AND s[i] == s[j] OR s[i] != s[j] AND f(i+1, j)
        # m, n = len(s), len(t)
        # f(i, n) = 1, f(m , j) = 0
        memo = {}

        def distinctSubsequence(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = distinctSubsequence(i+1, j) + distinctSubsequence(i+1, j+1)
            else:
                memo[(i, j)] = distinctSubsequence(i+1, j)

            return memo[(i, j)]
        
        return distinctSubsequence(0, 0)

    
            