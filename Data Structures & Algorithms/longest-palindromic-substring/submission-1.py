class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        start = 0
        max_length = 1

        def palindromeCheck(i, j):
            nonlocal start, max_length
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = (s[i] == s[j]) and palindromeCheck(i + 1, j - 1)
            if memo[(i, j)]:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    start = i
            return memo[(i, j)]
        for i in range(len(s)):
            for j in range(i, len(s)):
                palindromeCheck(i, j)
        return s[start : start + max_length]
