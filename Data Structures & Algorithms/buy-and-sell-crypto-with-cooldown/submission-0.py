class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # holding = 0 
        # choices = buy, not buy.
        # holding = 1
        # choices = hold, sell.
        # if holding = 0 right after sell
        # choices = hold
        # f(i, 0) = (profit - prices[i]) -> f(i+1, 1) or profit -> f(i+1, 0)
        # f(i, 1) = profit -> f(i+1, 1) or (profit + prices[i]) -> f(i+2, 0)
        # f(i, 0) = max(f(i+1, 1)-prices[i], f(i+1, 0))
        # f(i, 1) = max(f(i+1, 1) or prices[i] + f(i+2, 0))
        n = len(prices)
        dp = [[0, 0] for _ in range(n+2)]
        
        for i in range(n-1, -1, -1):
            dp[i][0] = max(dp[i+1][0],-prices[i] + dp[i+1][1])
            dp[i][1] = max(dp[i+1][1], prices[i] + dp[i+2][0])
        return dp[0][0]
            
