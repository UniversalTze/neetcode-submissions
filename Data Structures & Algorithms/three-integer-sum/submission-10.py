class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sorted number O(N * LOG(N))
        res = []
        # no need to do the first index
        for index in range(1, len(nums)):
            cur = nums[index - 1]  # current number to check for 3Sum
            if index != 1 and prev == cur:  # so that duplicates are no longer attempted again
                continue
            # will find all possible combinations given the current index to the RHS of it
            # thus, the window can shrink after this has been completed
            if cur > 0:
                break # since array is sorted, all indexes past 0 cannot sum to 0 anymore
            start = index
            end = len(nums) - 1
            while start < end:
                if nums[start] + cur + nums[end] == 0: 
                    complete = [cur, nums[start], nums[end]]
                    res.append(complete)
                    check = nums[start]
                    while check == nums[start] and start < end: 
                        start += 1 # moves to next index where duplicates don't exist
                if nums[start] + cur + nums[end] > 0: 
                    end -= 1
                else: 
                    start += 1
            prev = cur
        return res
