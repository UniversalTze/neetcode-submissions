class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        # num courses represent how many courses you need to take 0 - n - 1
        # prerequisites of other courses can be found

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
                seen.remove(node)
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
