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

        while r < len(intervals):
            later = intervals[r]
            first = intervals[l]

            if later.start >= first.start and later.start < first.end:
                return False
            
            r+=1
            l+=1

        return True