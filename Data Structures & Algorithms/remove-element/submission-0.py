class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curIndex = 0
        for index in range(len(nums)):
            if nums[index] == val:
                continue
            nums[curIndex] = nums[index]
            curIndex += 1
        return curIndex

            
        