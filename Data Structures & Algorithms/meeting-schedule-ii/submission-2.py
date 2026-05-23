"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # idea get an array of start and stop times
        # only works when array is sorted. (twice) once for the start,
        # once for the end. 
        intervals.sort(key=lambda x: x.start)
        start = [i.start for i in intervals]
        intervals.sort(key=lambda x: x.end)
        end = [i.end for i in intervals]
        startp = 0
        endp = 0
        meeting = 0
        maxim = 0
        length = len(end)

        while startp != length and endp != length:
            if start[startp] < end[endp]:
                startp += 1
                meeting += 1
                maxim = max(meeting, maxim)
            elif end[endp] <= start[startp]:
                endp += 1
                meeting -=1
        return maxim
        