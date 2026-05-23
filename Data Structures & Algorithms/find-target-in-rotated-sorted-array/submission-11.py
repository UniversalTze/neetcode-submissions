class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check L and R to see which side is sorted
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (L + R)// 2
            if nums[mid] == target:
                return mid
            if nums[L] <= nums[mid]:
                # LHS is sorted, so check for conditions where L is brought up to mid
                if target > nums[mid] or nums[L] > target:
                    L = mid + 1
                else:
                    R = mid - 1
            else:
                # RHS side is ordered so find the conditions when 
                # target is not in the interval of the ordered section
                if nums[mid] > target or nums[R] < target:
                    R = mid - 1
                else:
                    L = mid + 1
        return -1






        