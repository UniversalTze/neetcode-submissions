class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        if len(nums) == 1:
            return nums[0]
        # [3, 4, 5, 6]
        def helper(nums: List[int]):
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for index in range(2, len(nums)):
                dp[index] = max(dp[index - 1], nums[index] + dp[index - 2])
            return dp.pop()
        return max(helper(nums[1:]), helper(nums[:-1]))




            


                

        