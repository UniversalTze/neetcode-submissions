class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list in ascending order 
        nums.sort() # in place so O(1) space and o(N Log N) worst case time

        # sorted means 0 is our seperator. If index goes above 0, cases will no longer sum to 0
        # as summation of 3 positive numbers can never be 0. 

        result = [] # store results of all 3 sums that add to 0. 

        for index in range(len(nums)):
            if nums[index] > 0: 
                break
            # to stop duplicates triplets entry, 
            # if current is equal to previous one, we have already got the combination of 
            # sums so it can be skipped
            if index > 0 and nums[index] == nums[index - 1]: 
                continue

            # can use two pointer approach where second pointer starts at index + 1
            # other pointer starts the end of the array and moves backwards
            start, end = index + 1, (len(nums) - 1)

            # we only care about all indexes to the right of the array as indices must all be unique
            # when we've visited current index all possible combinations of 3 sum to 0 has been found
            # so no need to include these for further iterations in inner loops
            while start < end: 
                if nums[index] + nums[start] + nums[end] < 0:
                    # means the number at starting index is too negative, move start pointer forward
                    start += 1
                elif nums[index] + nums[start] + nums[end] > 0:
                    # too positive, so need to move end index down
                    end -= 1
                else: 
                    # sums to zero, so add to triplet array
                    result.append([nums[index], nums[start], nums[end]])
                    end -= 1 # decrement end index
                    foundstart = nums[start]
                    while start < end and nums[start] == foundstart: 
                        # find a new index that is off distinct value so that
                        # resulting triplets are not duplicates in result
                        start += 1
        return result


         
            
        