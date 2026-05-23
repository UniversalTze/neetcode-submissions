class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        # sorted intervals sort so that we can detect overlapping intervals
        removed = 0

        end = intervals[0][1]
        for index in range(1, len(intervals)):
            cur = intervals[index]
            start = cur[0]
            curEnd = cur[1]
            if start < end:
                removed += 1
                end = min(end, curEnd)
            else:
                end = curEnd

        return removed
        