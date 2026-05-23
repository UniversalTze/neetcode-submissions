class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for index in range(len(nums)): 
            if nums[index] not in seen:
                seen[nums[index]] = index
            else:
                return True
        return False
        