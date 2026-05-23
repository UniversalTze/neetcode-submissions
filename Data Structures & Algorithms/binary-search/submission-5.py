class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O (log N) time
        start = 0
        end = len(nums) - 1
        while start <= end: 
            # mid = start + (end - start) // 2 (good for larger constrains and other languages with fixed size unsigned and signed ints)
            # python has no fixed sized integers
            mid = (start + end) // 2    # can lead to overflow in other languages
            if nums[mid] == target:
                return mid

            if nums[mid] < target: 
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return -1



        