class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2 # floor division
        while start <= end: # can be equal [5]
            # start = 0, end = 5, mid = 5//2 array: [-1,0,2,4,6,8] target = 3. 3 > 2
            # start = 3 (2 + 1), end = 5, mid = 4, array[mid] = 6 > 3
            # start = 5, end = 5, mid = 5 + 5 // 2 = 5
            # array[5] = 8 < 3, start = mid + 1 = 6 (start > end) (exit loop)
            # find another case when start and end are same index
            # start = 1, end = 1, mid = 1 + 1 // 2 = 1 (check)
            if nums[mid] > target: 
                end = mid - 1
            elif nums[mid] < target: 
                start = mid + 1
            else:
                return mid
            mid = (end + start) // 2
        return -1
        