class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log N) time complexity (worst case is O(N) if sorted)
        # O(1) space
        start = 0 # get the first element of the list
        # as the list has been sorted (even through rotation)
        # we know that if the start of the list is larger than 
        # it's been rotated so we move back towards that side using binary search
        mid = len(nums) // 2 # middle point of array
        end = len(nums) - 1 # have the end of the list
        maxIndex = -1
        
        # No need to find maximums of the array
        while start < end:
            # if start == end (break out of loop)
            checkleft = nums[start] # check LHS 
            midpoint = nums[mid] # check middle

            if checkleft < midpoint: 
                # can't disregard mid point here as it may the largest elemt in list
                # so set start to be mid
                start = mid
            elif nums[end] > checkleft: # if end of the array is currently larger than checkleft (start of array/shrinked window)
                start += 1 # basically for the case when array is perfectly rotated (Bad!) (Worst case is O(N))
            else: 
                # checkleft > midPoint
                end = mid - 1
            mid = (start + end) // 2
        # start index will hold the maxIndex of the current array   

        maxIndex = start 
        if maxIndex < len(nums) - 1: 
            result = nums[maxIndex + 1]
        else: 
            result = nums[0] # overflow (base case)
        return result



        