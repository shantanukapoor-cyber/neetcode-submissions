class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # f(i) = if f(i-1) > 0 f(i-1) else 0 + nums[i]
        # f(0) = nums[0]
        # where f(i) is the maximum possible sum at i.
        n = len(nums) 
        dp = [0] * n
        dp[0] = nums[0]
        maximum_sum = dp[0]
        for i in range(1, n):
            dp[i] = nums[i]
            if dp[i-1] > 0:
                dp[i] += dp[i-1]
            maximum_sum = max(maximum_sum, dp[i])
        return maximum_sum
