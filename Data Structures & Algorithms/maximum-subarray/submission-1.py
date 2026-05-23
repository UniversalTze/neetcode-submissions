class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        # one base case (doesn't matter)
        # we know that anything that goes below 0 can be forgotten or not
        # apart of the max sub-array
        
        # what we want to do is keep a max variable and query it at each operation
        # we know that it goes negative, it won't be apart of max array as it drags the max value
        index = 0
        curSum = 0
        maxSum = float("-inf")
        while index < len(nums):
            curSum = curSum + nums[index] # just add the current number
            maxSum = max(curSum, maxSum) # replace max if needed (negative numbers can now work with this loop)
            if curSum < 0:
                # we know that negative number can only subtract away from the possible maximum
                # thus, we be greedy and not include this current element, thus resetting curSum to 0. 
                curSum = 0
            index += 1
        return maxSum
                        