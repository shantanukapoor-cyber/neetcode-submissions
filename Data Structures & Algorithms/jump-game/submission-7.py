class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i <= max_reach:
                max_reach = max(max_reach, i + nums[i])
        if max_reach >= n-1:
            return True
        else:
            return False
