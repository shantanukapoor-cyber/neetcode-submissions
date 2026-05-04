class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0) 
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = i - left - 1
                area = height * width
                max_area = max(area, max_area)
            stack.append(i)
        return max_area