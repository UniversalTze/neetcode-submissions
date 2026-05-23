class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxarea = 0

        while left < right:
            width = right - left

            height = min(heights[left], heights[right])
            maxarea = max(maxarea, width * height)
            if heights[left] < heights[right]: 
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxarea
        