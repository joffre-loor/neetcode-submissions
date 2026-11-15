"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l, r = 0, 1
        intervals.sort(key=lambda i : i.start)
        while r < len(intervals):
            later = intervals[r]
            first = intervals[l]
            
            if first.end > later.start:
                return False

            r+=1
            l+=1

        return True