class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}  # Stores results we already found

        def ways(m):
            if m in memo:
                return memo[m]  # Return saved answer
            if m >= n:
                return 1 if m == n else 0

            # Save the answer before returning it
            memo[m] = ways(m + 1) + ways(m + 2)
            return memo[m]

        return ways(0)
