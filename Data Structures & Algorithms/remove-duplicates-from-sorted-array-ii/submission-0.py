class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        MAXCOUNT = 2

        current = nums[0]
        recurCount = 1
        removeCount = 0

        for index in range(1, len(nums)):
            if current != nums[index]:
                # reset the count if a new number is seen (ordere arr)
                current = nums[index]
                recurCount = 1
            else:
                recurCount += 1
            
            if recurCount > MAXCOUNT:
                removeCount += 1
            nums[index - removeCount] = current
        return len(nums) - removeCount



        