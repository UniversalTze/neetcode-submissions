class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # returning True if you can get to the last index or above last index of the list
        goal = len(nums) - 1
        if len(nums) == 1:
            return True
        if not nums[0]: 
            # if first index is 0, you can't move, therefore you cannot reach the end from 0
            return False
        # [n - 2, n - 1 = 0, n]
        #for index in range (len(nums)):
        for index in range(len(nums) - 1, -1, -1):
            # go down to 0 and move through the array backwards
            # instead of checking from the start, since we will need
            # to check for range of max jump, e.g for 3, you need to check paths of 1,2
            # if the maximum (3) cannot make it there

            # therefore, a better way is to go backwards. 
            # if current index + steps at index surpasses or reaches the goal, we know that 
            # we just need to get to that goal (being greedy), we set that index as the new goal
            # Thus, this new way of checking runs in O(N) instead of O(N^2 * N) where n^2 is the 
            # number of possible paths and N is the number of nodes in the list.  
            steps = nums[index]
            if steps + index >= goal:
                goal = index

        if goal == 0:
            return True
        return False



        

        


        