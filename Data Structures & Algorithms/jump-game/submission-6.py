class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # brute force it
        # all possible up to n, so lets say that n is the largest number possible\
        # has to test all of n to see if it can reach the goal or not. 
        # which is O(N^2), n + n - 1 + n - 2 + .....1 = arithmetic sequence

        # instead of going forwards, we go backwards.
        # if the current index can reach the goal, we can forget about the goal 
        # and make the goal that current index. Update the index of goal.
        # goal is to try and reach end index
        goal = len(nums) - 1
        for index in range(goal - 1, -1, -1):
            # going backwards from goal
            jump = nums[index]
            if index + jump >= goal:
                goal = index
        return goal == 0
        