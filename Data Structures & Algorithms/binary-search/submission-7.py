class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2
        while start <= end: # can be equal [5]
            # start 0, end = 1, mid = 0
            if nums[mid] > target: 
                end = mid - 1
            elif nums[mid] < target: 
                start = start + 1
            else:
                return mid
            mid = (end + start) // 2
            # mid = 1 + 1 // 2 = 1
        return -1
        