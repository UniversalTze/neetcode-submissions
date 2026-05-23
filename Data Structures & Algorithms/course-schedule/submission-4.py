class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # num courses represent how many courses you need to take 0 - n - 1
        # prerequisites of other courses can be found

        # seen set just the necesary prereqs for a course
        def cycledfs(seen, cur):
            nonlocal preMap
            if cur in seen:
                return True
            if cur not in preMap: # means no cycles have occured can return
                seen.add(cur)
                return False
            # get prereqs of current node
            neighbours = preMap[cur]
            seen.add(cur)
            for node in neighbours:
                cycle = cycledfs(seen, node)
                if cycle:
                    return True
                seen.remove(node) # remove node after backtracking from dfs
                # as seen nodes must capture what has been seen at that time
                # e.g [[0,1],[0,2],[1,3],[2,3],[3,4]
                # prereq Map: {0 : [1,2], 1:[3], 2:[3], 3:[4]}
                # When we do dfs, we go down one path first. When we get to 0
                # there is 2 "prereqs", we go down 1 which leads to a set formation:
                # seen: 1: {0}, 2nd iteration {0,1}, 3rd iteration: {0,1,3,4}

                # however if we don't we remove from the set, when we traverse down 2 prereqs,
                # 3 is already in the set causing a false positive cycle, leading to incorrect result. 
                # as 3 or 4 is not a prereq of 2.  Only 0 should be in the set when it gets
                # to navigating down 2's prereq and trying to find a cycle. 
            return False

        preMap = {}
        # hold a map of prereq courses to courses that need to be completed. 
        for prereqs in prerequisites:
            # meaning of this map, in order to take course in p[0], take p[1] first
            preMap.setdefault(prereqs[0], []).append(prereqs[1])

        res = numCourses - 1
        # use a dfs function to go through the map if prereqs arise
        # keeping track of completed courses
        while res >= 0: 
            if res not in preMap:
                # no prereqs for this course
                res -= 1 
                continue
            # need to do a dfs and check if course has been completed
            # if a reference on a course that has not been completed 
            # then return false
            courseCompleted = set()
            # do a dfs on current node checking prereqs
            if cycledfs(courseCompleted, res):
                return False
            res -= 1


        return True
