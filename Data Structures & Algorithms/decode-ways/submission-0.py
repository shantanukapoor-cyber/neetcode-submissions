class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def f(i):
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            # Take 1 digit (always valid here since s[i] != '0')
            ways = f(i + 1)

            # Take 2 digits (if in range 10-26)
            if i + 1 < n and int(s[i:i+2]) <= 26:
                ways += f(i + 2)

            memo[i] = ways
            return ways

        return f(0)