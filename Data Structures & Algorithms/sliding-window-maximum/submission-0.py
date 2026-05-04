class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # move the window, push the maximum to the result.
        # when the window leave time has come,
        # which means each max value will have TTL attached.
        stack = deque()
        start = 0
        result = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            stack.append(i)
            if start > stack[0]:
                stack.popleft()
            if i + 1 >= k:
                result.append(nums[stack[0]])
                start += 1
        return result   

        