class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        tx, ty = intervals[0]
        answer = []
        for i in range(1,len(intervals)):
            a, b = intervals[i]
            if a <= ty:
                ty = max(ty, b)
            else:
                answer.append([tx, ty])
                tx, ty = a, b
        answer.append([tx, ty])
        return answer
