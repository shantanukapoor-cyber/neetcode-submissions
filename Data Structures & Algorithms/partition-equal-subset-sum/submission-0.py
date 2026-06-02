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
        # if yes then true.
        total_sum = sum(nums)
        n = len(nums)
        if total_sum % 2 != 0:
            return False
        individual_sum = total_sum // 2
        def is_subset_sum_exists(arr, k):
            # Create a DP array tracking reachable sums from 0 to k
            dp = [False] * (k + 1)
            dp[0] = True  # Base case: A sum of 0 is always possible (empty subset)

            for num in arr:
                # Update dp array backwards to prevent using the same element twice
                for j in range(k, num - 1, -1):
                    if dp[j - num]:
                        dp[j] = True
                        
            return dp[k]

        return is_subset_sum_exists(nums, individual_sum)