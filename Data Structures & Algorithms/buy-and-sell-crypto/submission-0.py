class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_buy_price = prices[0]
        for end in range(len(prices)):
            profit = prices[end]-min_buy_price
            maxProfit = max(profit, maxProfit)
            min_buy_price = min(prices[end],min_buy_price)
        return maxProfit