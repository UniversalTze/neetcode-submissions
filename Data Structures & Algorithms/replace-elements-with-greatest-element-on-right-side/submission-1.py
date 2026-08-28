class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        index = len(arr) - 1
        maximum = -1
        # set last element of array to -1
        res[index] = maximum
        index -= 1
        while index >= 0:
            maximum = max(maximum, arr[index + 1])
            res[index] = maximum
            index -= 1
    
        return res