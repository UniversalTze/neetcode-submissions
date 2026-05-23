class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (end + start) // 2 # floor division
        while start <= end: # can be equal [5]
            # start 6, end = 0, mid = 3 array: [-1,0,2,4,6,8] target = 3. 3 < 4
            # 
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
        