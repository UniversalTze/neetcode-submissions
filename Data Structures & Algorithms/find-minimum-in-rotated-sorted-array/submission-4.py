class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # when something has been rotated (one side of the array will be sorted, while the other is not)
        # use mid point to detect if array is sorted
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                # RHS is sorted so, the minimum element cannot be there
                # e.g [4, 5, 1, 2, 3], 1 < 3
                # tells us that minimum element cannot be on RHS as its ordered
                # e.g [3, 4, 5, 1, 2], 5 < 2 so minimum element will occur on LHS
                # as that part of the array is not ordered. (RHS 3,4,5 is ordered tho)
                # the minimum element is the first element of the rotated portion.
                # as RHS is sorted, rotation has not affected it
                # m is inclusive as m might still be minimum element
                r = m
            else:
                # nums[m] > nums[r]
                # therefore m index can't be minimum m can be excluded. 
                l = m + 1
        return nums[l]



        