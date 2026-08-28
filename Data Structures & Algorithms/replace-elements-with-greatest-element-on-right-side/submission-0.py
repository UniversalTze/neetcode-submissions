class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        index = len(arr) - 1
        maximum = -1
        # set last element of array to -1
        res[index] = maximum
        index -= 1
        while index >= 0:
            res[index] = max(maximum, arr[index + 1])
            if arr[index + 1] > maximum:
                maximum = arr[index + 1]
            index -= 1
    
        return res