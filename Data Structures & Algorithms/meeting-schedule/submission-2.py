"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # no space (but bad thing is I modified original array)
        attend = True
        if len(intervals) < 2: 
            return attend
        # best case it to sort array so that you are dealing with intervals that incrementally increase
        intervals.sort(key=lambda x: x.start) # O(Nlog(n))
        # intervals now is sorted
        mintime, maxtime  = 0, 0
        for interval in intervals:
            if mintime == 0 and maxtime == 0:
                mintime = interval.start
                maxtime = interval.end
                continue
            if interval.start == mintime:
                return False
            if interval.start < maxtime:
                return False
            mintime = interval.start
            maxtime = interval.end

        return attend
