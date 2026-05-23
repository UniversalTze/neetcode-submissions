class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use mid to determine which side of the array to look
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid 
            # nums[start] and index may be the same in a array lenth of 2
            if nums[start] <= nums[mid]: # check if array is ordered on LHS
                # LHS is sorted
                # two cases for searching end of array:
                # 1. target if above the middle of array (in other side, given its sorted)
                # 2. start of the array is above the target
                if target > nums[mid] or nums[start] > target:
                    start = mid + 1
                else:
                    end = mid - 1
            # RHS is sorted array e.g [5,1,2,3,4]
            else: 
                # check the other half on specific conditions
                # if nums[mid] > target, target should be on LHS. 
                # For cases like: [5,1,2,3,4] when target = 1
                # or when nums[end] < target, meaning its on LHS
                if nums[mid] > target or nums[end] < target: 
                    end = mid - 1
                else: 
                    start = mid + 1

        
        return -1


        