class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the interval.
        # now pick queries[i].
        # set max_len = float('inf')
        # go until queries[i] < 
        intervals.sort()
        tx, ty = intervals[0]
        answer = []
        for query in queries:
            if query < tx:
                answer.append(-1)
                continue
            min_value = float('inf')
            for interval in intervals:
                a, b = interval
                if a <= query <= b:
                    updated_len = b - a + 1
                    min_value = min(min_value, updated_len)
            if min_value == float('inf'):
                answer.append(-1)
            else:
                answer.append(min_value)
        return answer
