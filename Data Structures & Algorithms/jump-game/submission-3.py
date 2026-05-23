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
            # go down 0 and do it backwards
            steps = nums[index]
            if steps + index >= goal:
                goal = index

        if goal == 0:
            return True
        return False



        

        


        