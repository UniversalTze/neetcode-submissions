class Solution:
    def trap(self, height: List[int]) -> int:
        rainwater = 0
        prefix = [] # prefix and suffix array of current index
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
            mini = min(prefix[index], suffix[index])
            print(mini)
            
            rainwater += min(prefix[index], suffix[index]) - height[index]
            print(rainwater)
        return rainwater
        