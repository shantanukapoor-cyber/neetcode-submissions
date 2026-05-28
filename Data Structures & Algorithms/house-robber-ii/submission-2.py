class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case for a single house
        if len(nums) == 1:
            return nums[0]
            
        # This is your exact House Robber 1 code!
        def rob_linear(houses):
            memo = {}
            def maxCost(index):
                if index >= len(houses):
                    return 0
                if index in memo:
                    return memo[index]
                x = maxCost(index + 2) + houses[index]
                y = maxCost(index + 1)
                memo[index] = max(x, y)
                return memo[index]
            return max(maxCost(0), maxCost(1))

        # Cut the circle into two straight lines and take the best one
        option1 = rob_linear(nums[:-1])  # Skip last house
        option2 = rob_linear(nums[1:])   # Skip first house
        
        return max(option1, option2)
