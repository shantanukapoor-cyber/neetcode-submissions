class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removal = 0
        ty = intervals[0][1]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if a < ty:
                removal += 1
                ty = min(ty, b)
                continue
            ty = b
        return removal