class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sum the first combination up to n. 
        # e.g [2,5,6,9]
        # 2 + 2 + 2 + 2 + 2 > 9
        # pop a 2 off, then do + 5.
        # base condition: if number > target then backtrack

        res = [] # resulting
        # backtrack mainly uses recursion. Go down the tree, then backtrack with the options. 

        # cur is an array that holds all the numbers that have been used to add
        # index is used to keep up to show what has been excluded so that no duplicates
        # is returned
        # total is used to help keep track of what has been added to it. 
        def dfs(index, cur, total):
            nonlocal res
            if total == target: 
                res.append(cur.copy()) # copy as this may change throughout array
                return
            if index >= len(nums) or total > target: 
                return
            # two decisions
            cur.append(nums[index])
            dfs(index, cur, total + nums[index])
            cur.pop() 
            dfs(index + 1, cur, total)
        dfs(0, [], 0)
        return res
                
        

        