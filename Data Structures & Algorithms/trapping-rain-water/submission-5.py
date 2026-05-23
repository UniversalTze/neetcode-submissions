class Solution:
    def trap(self, height: List[int]) -> int:
        # using two pointers one at the start (left most)
        # another one on the end (right most)
        # O(N) time and O(1) space

        # main idea:
        # Move start or end pointer depending on which on has the highest max
        # if same, have the choice to decide which pointer to advance

        # when a new max on left occrus, update left max. If left > right,
        # then move right pointer back. This is because when we find a rightmax = or > leftMax then 
        # any index to the right of leftMax in height that is below current Leftmax 
        # can hold max - height[index] units of water
        # this is why we move left and right pointers depending on their current max
        
        # this same idea applies to the right (except for items towards the left of right max)

        # e.g if we have a Leftmax of 2 and right max of 1. Move rightmax until its bigger than Leftmax
        # This is because when we find a height equivalent to Leftmax or bigger, 
        # min(leftmax, rightmax) - height[index] units of water can be stored for all indexes in between
        # index of left and right max
        # when start >= end (everything has been visited in array)

        storage = 0
        start, end = 0, len(height) - 1
        leftMax = height[start] # set maxes to the first and last element in the array
        rightMax = height[end]

        while start < end:
            if leftMax <= rightMax: 
                # if left max is smaller or equal to right max
                start += 1
            elif leftMax > rightMax: 
                # left max is currently larger, so need to locate a right max that is larger
                end -= 1

            if leftMax - height[start] > 0: 
                # if current left iteration find a shorter height
                # use minimum of left and right boundaries
                storage += min(leftMax, rightMax) - height[start]
            else: 
                leftMax = height[start]
            
            if rightMax - height[end] > 0: 
                # if current right iteration find a shorter height
                # use minimum of left and right boundaries
                storage += min(leftMax, rightMax) - height[end]
            else: 
                rightMax = height[end]
            
        return storage
        

        