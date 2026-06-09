class Solution:
    def jump(self, nums: List[int]) -> int:
        # [0] * n
        # f(i) = minimum to reach i
        # 
        n = len(nums)
        farthest = 0
        current_end = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
            
        