class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log N) time complexity
        start = 0 # get the first element of the list
        # as the list has been sorted (even through rotation)
        # we know that if the start of the list is larger than 
        # it's been rotated so we move back towards that side using binary search
        mid = len(nums) // 2 # middle point of array
        end = len(nums) - 1
        maxIndex = -1
        
        # No need to find maximums of the array
        while start < end:
            checkleft = nums[start]
            midpoint = nums[mid]
            #print(checkleft)
            #print(midpoint)
            if checkleft < midpoint: # can't disregard mid point here as its the largest element
                start = mid
            elif nums[end] > checkleft:
                start += 1
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



        