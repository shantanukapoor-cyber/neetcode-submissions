class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def minCost(steps):
            if steps >= len(cost):
                return 0 
            if steps in memo:
                return memo[steps]
            x = cost[steps] + minCost(steps + 1)
            y = cost[steps] + minCost(steps + 2)
            memo[steps] = min(x, y)
            return memo[steps]
        return min(minCost(0), minCost(1))