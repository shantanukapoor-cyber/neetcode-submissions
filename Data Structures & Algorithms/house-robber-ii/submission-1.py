class Solution:
    def rob(self, nums: List[int]) -> int:
        # circular rob index = x % len(nums)
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def maxCost(index, z_start):
            if index >= len(nums):
                return 0
            if (index,z_start) in memo:
                return memo[(index,z_start)]
            if index == len(nums) - 1:
                if z_start:
                    return 0 # Can't rob it if we robbed house 0
                else:
                    return nums[index] # Can rob it safely
            # pick
            x = maxCost(index+2, z_start) + nums[index]
            # skip
            y = maxCost(index+1, z_start)
            memo[(index,z_start)] = max(x, y)
            return memo[(index,z_start)]
        return max(maxCost(0, True), maxCost(1, False))