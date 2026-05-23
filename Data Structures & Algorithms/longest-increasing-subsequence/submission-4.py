class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1 is assigned to all indexes as each item is a sub sequence
        dparray = [1] * (len(nums))
        maxseq = 1
        maxnum = float("-inf")
        minimum = nums[0]
        for index in range(1, len(nums)):
            if nums[index] < minimum:
                minimum = nums[index]
                continue
            if nums[index] > nums[index - 1]:
                if nums[index] > maxnum:
                    dparray[index] = maxseq + 1
                    maxnum = nums[index]
                else:
                    dparray[index] = dparray[index - 1] + 1
                    maxnum = max(maxnum, nums[index])
            else:
                if nums[index] == minimum:
                    #print("erer")
                    # if minimum, just set it to be current max sequence
                    dparray[index] = maxseq
                    continue
                counter = index - 1
                while counter > -1:
                    if nums[counter] <= nums[index]:
                        break
                    counter -= 1
                if nums[counter] < nums[index]:
                    dparray[index] = dparray[counter] + 1
                else:
                    dparray[index] = dparray[counter]
                
            maxseq = max(dparray[index], maxseq)
        print(dparray)
        return maxseq
        