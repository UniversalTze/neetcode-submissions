class Solution:
    def trap(self, height: List[int]) -> int:
        # O(N) space and O(N) time solution
        
        # base logic: just need two walls to the left and right of the current
        # index to be able to store the water.
        # when this occurs, you want to find the minimum height of L and R walls and
        # then subtract it by current index to see how much water can held in those rows
        rainwater = 0
        # prefix: hold maxes off all prefixes upto and including current index
        # (to the left)
        prefix = [] # prefix and suffix array of current index
        # suffix: hold maxes off all suffixes upto and including current index
        # to the left
        suffix = [0] * len(height)
        for index in range(len(height)):
            if index == 0: 
                prefix.append(height[index])
            elif prefix[-1] < height[index]:
                prefix.append(height[index])
            else:
                element = prefix[-1]
                prefix.append(element)
            
        for index in range(len(height) - 1, -1, -1):
            if index == len(height) - 1:
                suffix[index] = height[index]
            elif suffix[index + 1] < height[index]:
                suffix[index] = height[index]
            else: 
                element = suffix[index + 1]
                suffix[index] = element
        print(prefix)
        print(suffix)
        for index in range(len(height)):
            rainwater += min(prefix[index], suffix[index]) - height[index]
        return rainwater
        