class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2) 
        length = len(nums)
        for i in range(len(nums)):
            res[i] += nums[i]
            res[i + length] += nums[i]
        return res
        