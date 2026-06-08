class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # .  -> skip
        # * -> match with j-1
        # f(i, j) -> where i is the s and j is the p.
        # p can either be letter, ., letter*
        # so we can either get letter - letter,
        # letter - .
        # letter - letter*
        # 1. match f(i, j) -> f(i+1, j+1)
        # 1. mismatch f(i, j) -> False
        # 2. doesn't matter f(i, j) -> f(i+1, j+1)
        # 3. if j+1 is *,
        # 3. match f(i, j) -> f(i+1, j)
        # 3. mismatch f(i, j) -> f(i, j+2)
        # f(m, n) = True
        # f(i, n) = False
        # f(m, j) = False or if j+1 == * then f(m, j+2)
        m, n = len(s), len(p)
        memo = {}

        def regexMatch(i, j):
            if j == n:
                if i == m:
                    return True
                if i < m:
                    return False
            if i == m:
                if j < n:
                    if j+1 < n and p[j+1] == '*':
                        return regexMatch(m, j+2)
                    else:
                        return False
            if (i, j) in memo:
                return memo[(i, j)]
            if j+1 < n and p[j+1] == '*':
                memo[(i, j)] = regexMatch(i, j+2)
                if s[i] == p[j] or p[j] == '.':
                    memo[(i, j)] = memo[(i, j)] or regexMatch(i+1, j)
            else:
                if s[i] == p[j] or p[j] == '.':
                    memo[(i, j)] = regexMatch(i+1, j+1)
                else:
                    memo[(i, j)] = False
            return memo[(i, j)]

            

        
        return regexMatch(0, 0)


