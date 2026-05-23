class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # so iterate backwards
        # doing this with a bottom up approach
        # to unambiguously solve the question, 
        # we understand, that the sequence is as long as the final 
        # character, thus, we go backwards, to remove that unambiguity of the longest increasing 
        # sequence
        dparr = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for y in range(i + 1, len(nums)):
                if nums[i] < nums[y]:
                    LIS = max(dparr[i], dparr[y] + 1)
                    dparr[i] = LIS
        return max(dparr)

        