class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0,0,2,2,3,3,3,3,3,3]
        suffix_max = [3,3,3,3,3,3,3,2,1,0]

        prefix_max = []
        value_prefix = 0
        for i in range(len(height)):
            prefix_max.append(value_prefix)
            value_prefix = max(value_prefix, height[i])
        suffix_max = []
        value_suffix = 0
        for i in range(len(height)-1,-1,-1):
            suffix_max.append(value_suffix)
            value_suffix = max(value_suffix, height[i])
        suffix_max.reverse()
        area = 0
        for i in range(len(height)):
            water = min(prefix_max[i], suffix_max[i]) - height[i]
            if water > 0:
                area += water
        return area

        