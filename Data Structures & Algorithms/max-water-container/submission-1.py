class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(N) time and O(1) space
        left = 0
        right = len(heights) - 1
        maxarea = 0

        while left < right:
            width = right - left

            height = min(heights[left], heights[right])
            maxarea = max(maxarea, width * height)
            # convention up to user, but can do this one
            # if heights[left] < heights[right]: 
            if heights[left] <= heights[right]: 
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            """
            additional else if the first if (commented out is used)
            else: 
                left += 1
                right -= 1
            """
        return maxarea
        