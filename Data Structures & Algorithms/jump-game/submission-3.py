class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # f(i) = OR f(i + nums[i])
        # f(i) is whether we can reach n-1 from i
        # f(n-1) = True
        # if f(i + nums[i]) > n - 1 then False
        # nums[i] is maximum jumps possible from i
        # so f(i) = f(i+1) or f(i+2) or ... or f(i+nums[i])
        # or f(i) = can reach i from 0 or not.
        # f(0) = true
        # f(1) = f(nums[0])
        # so whatever is f(0), set those future jumps to true.
        # start [True, False, False, False, ...]
        # for each True value,
        # set future nums[i] values to True
        # go to next term.
        # do this until you get false.
        # return dp[-1]
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        i = 0
        while dp[i] == True:
            if i == n-1:
                break
            if nums[i] > 0:
                boundary = min(n - i, nums[i] + 1)
                for j in range(1, boundary):
                    dp[i + j] = True
            i = i + 1
        return dp[-1]
