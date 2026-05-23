class Solution:
    def rob(self, nums: List[int]) -> int:
        # there's no need to do it through recursion. It just makes it hard
        # for these dp, its drawing out the decision trees and how you can apply that 
        # to normal datastructures. 
        arr = [0] * len(nums)
        rob1, rob2 = 0, 0
        maximum = 0
        for index in range(len(nums)):
            # first 2 house, the maximum values are their index
            if index < 2: 
                arr[index] = nums[index]
                maximum = max(maximum, nums[index])
                continue
            if index == 2: 
                arr[index] = nums[index] + arr[index - 2] 
                maximum = max(arr[index], maximum)
                continue
                # the first index as third index can only add the first one or not rob at all
            else: 
                rob1 = arr[index - 3]
                rob2 = arr[index - 2]
                maxrob = max(rob1, rob2)
                arr[index] = maxrob + nums[index]
                maximum = max(arr[index], maximum)
                
            # as you move past these 2 values, the index will represent the maximum 
            # amount that can be stolen
            # e.g 3rd index will be the sum of 1 and 3.
            # 4th index will be the max of 1 and 3 or 2 and 4 and then so on. 
            
        return maximum

            