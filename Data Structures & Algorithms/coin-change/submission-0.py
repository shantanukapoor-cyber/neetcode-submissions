class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(amount) = 1 + f(amount - coins[amount]) and amount - coins[amount] > 0 
        # if  we choose coins[amount]
        memo = {}
        def ways(remaining):
            if remaining < 0:
                return -1
            if remaining  == 0:
                return 0
            if remaining in memo:
                return memo[remaining]
            min_way = float('inf')
            for coin in coins:
                new_amount = remaining - coin
                possibility = ways(new_amount)
                if possibility != -1:
                    min_way = min(min_way, possibility + 1)
            memo[remaining] = min_way if min_way != float('inf') else -1
            return memo[remaining]
        return ways(amount)


