class Solution:
    def trap(self, height: List[int]) -> int:
        # given an array of numbers that represent height
        # to brute it, naive idea, is at current iteration, 
        # keep going through array until you find another max, update it 
        # and then going through, calculating the water stored at each lower heights. 

        # what is bad about this approach -> Does not consider local min and maxes

        # To change this approach, we can use two pointer approach. In this approach, we understand that 
        # if we have a left index of 2 (e.g), all we need coming from the right is something that is 2 or greater
        # there we are able to have a wall where water is stored
        # And we know that water can only be stored at the minimum of L and R

        # we know that the borders can't store water, so we start indexes 1 in. 
        left, right = 1, len(height) - 2
        waterTrapped = 0
        curLeft = height[0]
        curRight = height[len(height) - 1]
        while left <= right:
            curLeft = max(height[left], curLeft)
            curRight = max(height[right], curRight)

            if curLeft < curRight:
                waterTrapped += min(curLeft, curRight) - height[left]
                left += 1
            else:
                # if left and right are equal, move right pointer back
                waterTrapped += min(curLeft, curRight) - height[right]
                right -= 1
        return waterTrapped
        # solution O(N) time and O(N) space




        