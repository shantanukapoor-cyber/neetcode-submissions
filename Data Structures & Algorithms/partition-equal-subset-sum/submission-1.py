class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # if sum(subset1) == sum(subset2)
        # first thing that will always be true is total sum is even.
        # if it's odd we can straight away mark it as false.
        # if it's even. each mutually exclusive subset should have
        # sum as total_sum//2.
        # so we need to do is find a way to check whether
        # there exists a subset whose sum of elements is total//2
        # and sum of it's complement is also the same.
        # if found subset sum = total // 2 then true.
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2 != 0:
            return False
        individual_sum = total_sum // 2
        # f(i, s) = f(i-1, s) or f(i-1, s-n[i])
        dp = [[False] * (individual_sum+1) for _ in range(n+1) ]
        dp[0][0] = True
        for i in range(1,n+1):
            for s in range(individual_sum+1):
                dp[i][s] = dp[i-1][s]
                if s >= nums[i-1]:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-nums[i-1]]
        return dp[n][individual_sum]
