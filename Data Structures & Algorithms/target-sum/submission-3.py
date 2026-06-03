from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # nums[i] -> add current value or subtract current value
        # f(i) -> x + nums[i] -> f(i+1)
        # f(i) -> x - nums[i] -> f(i+1)
        # we need to find f(n) = target.
        # f(i, amount) = distinct ways to achieve amount at i
        # f(i, amount) = f(i-1, amount-nums[i-1]) + f(i-1, amount+nums[i-1])
        # f(0, 0) = 1
        
        @cache
        def f(i, amount):
            # Base Case: Used all numbers
            if i == 0:
                return 1 if amount == 0 else 0
                
            # Your exact relation: add current number OR subtract current number
            # nums[i-1] matches your 1-based indexing logic for the item choice
            return f(i - 1, amount - nums[i - 1]) + f(i - 1, amount + nums[i - 1])
            
        return f(len(nums), target)