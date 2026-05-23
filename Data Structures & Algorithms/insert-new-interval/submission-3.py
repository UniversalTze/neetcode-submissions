class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # we know that intervals is sorted by start time
        # assuming that starting intervals given is already valid
        res = []

        # two cases
        # 1. where new interval does not overlap with any other intervals -> means 
        # all intervals are returned as there is no overlap

        # 2. there is an overlap. Find the first interval, and the all the other 
        # ones within that range and then find maximum end time. 
        newIntStart = newInterval[0]
        newIntEnd = newInterval[1]
        appended = False
        for index in range(len(intervals)): 
            start = intervals[index][0]
            end = intervals[index][1]

            if start < newIntStart and end < newIntStart:
                res.append(intervals[index])
            elif start > newIntEnd and end > newIntEnd and not appended:
                # should only do this once (this case is for no intersection)
                res.append(newInterval)
                appended = True
                res.append(intervals[index])
            elif start > newIntEnd and end > newIntEnd:
                # for all cases larger than current interval
                res.append(intervals[index])

            else:
                # everything that's get to here is the intersection of the intervals
                # do a for loop here to find all intesections. 
                if not appended:
                    for count in range(index, len(intervals)):
                        curStart = intervals[count][0]
                        curEnd = intervals[count][1]
                        if curStart > newIntEnd:
                            # no longer an intersection here
                            break
                        start = min(newIntStart, curStart, start)
                        end = max(newIntEnd, curEnd)
                    # start time and end time of overlapping intervals have been found
                    res.append([start, end])
                    appended = True

        if not intervals or not appended:
            # if there is no current intervals, new interval can be added appended
            # if not currently appended, and above we've done checks for any intersection
            # then we just append the current interval as its valid and there no intersections
            # to be merged!!
            res.append(newInterval)
        return res

        