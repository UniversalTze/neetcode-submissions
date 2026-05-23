class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use mid to determine which side of the array to look
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid 
            if nums[start] <= nums[mid]: # check if array is ordered on LHS
                # LHS is sorted
                if target > nums[mid] or nums[start] > target:
                    start = mid + 1
                else:
                    end = mid - 1
            # RHS is sorted array
            else: 
                if nums[mid] > target or nums[end] < target: 
                    end = mid - 1
                else: 
                    start = mid + 1

        
        return -1


        