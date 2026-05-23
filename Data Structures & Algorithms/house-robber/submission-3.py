class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1]) # keeps the maximum profit of index 0 or 1
        for index in range(2, len(nums)):
            arr[index] = max(arr[index - 1], nums[index] + arr[index - 2])
        return arr.pop()