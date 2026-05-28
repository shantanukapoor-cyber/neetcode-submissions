class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def maxCost(index):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            # Pick
            x = maxCost(index+2) + nums[index]
            # Skip
            y = maxCost(index+1)
            memo[index] = max(x, y)
            return memo[index]

        return maxCost(0)