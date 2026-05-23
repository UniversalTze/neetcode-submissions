class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea if LHS is sorted, using start and mid point, we
        # have specific conditions to determine if it lies on the RHS
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                # Mid is apart of LHS sequence, now need to test if 
                # target is within that sequence
                # second condition is for when an array is ordered like
                # [1,2,3,4,5]
                # if mid < target, you know that target would lie on the right snd not the left
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else: 
                    r = mid - 1
            else:
                # RHS is ordered, mid is apart of the RHS and not the LHS
                if nums[r] < target or nums[mid] > target:
                    # second condition is for an array that has not been shifted
                    # whils the first one is used to identify given that array has been shifted
                    r = mid - 1
                else: 
                    l = mid + 1

        return -1

            







        