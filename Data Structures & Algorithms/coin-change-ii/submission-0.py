class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # f(i, amount) = distinct ways to get amount at index i
        # f(i, amount) = f(i-1, amount) + f(i, amount - coins[i])
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for s in range(amount+1):
                dp[i][s] = dp[i-1][s]
                if s >= coins[i-1]:
                    dp[i][s] += dp[i][s-coins[i-1]]
        return dp[n][amount]

