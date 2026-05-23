class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # idea: sort intervals
        # go one by one to keeping track of start and end. 
        res = {} # use a map with starting time leading to the intervals
        intervals.sort(key=lambda x: x[0])
        curstart = intervals[0][0] # first index is start of interval
        curend = intervals[0][1] # second index is end of interval
        res[curstart] = [curstart, curend]
        for index in range(1, len(intervals)):
            checkInt = intervals[index]
            checkStart = checkInt[0]
            checkEnd = checkInt[1]
            if checkStart <= curend:
                # use the curstart key as we have identified an overlap
                interval = res[curstart]
                curend = max(checkEnd, curend)
                interval[1] = curend
            else:
                curstart = checkStart
                curend = checkEnd
                res[curstart] = [curstart, curend]
        result = []
        for values in res.values():
            result.append(values)
        return result
        