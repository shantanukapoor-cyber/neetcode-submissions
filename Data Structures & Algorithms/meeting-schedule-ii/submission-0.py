"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda interval : interval.start)
        rooms = []
        for meeting in intervals:
            if rooms and rooms[0] <= meeting.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meeting.end)
        return len(rooms)


