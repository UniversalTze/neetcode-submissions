class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        posmap = {}

        for index in range(len(nums)):
            if nums[index] not in posmap:
                posmap[nums[index]] = index
            else:
                prevIndex = posmap[nums[index]]
                if index - prevIndex <= k:
                    return True
                posmap[nums[index]] = index
        return False
        