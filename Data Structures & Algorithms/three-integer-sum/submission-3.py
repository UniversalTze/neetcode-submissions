class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        checked = set()
        nums.sort() # sort the int array in ascending order

        # doing this means that we don't have to worry about inputs above 0 (duplicates aren't captured)
        # also need to use a set to check negative number set e.g [-2, -2, -1,0]
        # so no duplicates are found. Therefore, put result into a set. 
        for index in range(len(nums)): # o(N)
            # current equation is n1 + n2 + n3 = 0
            # rearrange to n1 = - (n2 + n3)
            # which can be transalted to -(n1) = n2 + n3
            # since array is sorted, 2 pointers can be used
            # add two cases
            # when start pointer moves above 0, no more options that can be added to target (0)
            # when end pointer moves below 0, no more options that can be added to target (0)
            # if index moves above 0, all cases have already been identified so can be terminated there
            if nums[index] > 0: 
                break
            if nums[index] in checked: 
                continue
            checked.add(nums[index]) # push to checked set for no iteration is repeated
            start = index + 1 #start pointer begins at current index + 1 (everything towards the right)
            end = len(nums) - 1 # end pointer (sorted so can use this technique)
            target = - (nums[index]) 

            while start < end: # o(N)
                if target == nums[start] + nums[end]: 
                    found = (nums[index], nums[start], nums[end])
                    result.add(found)
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                    continue
                if nums[start] + nums[end] < target:
                    # move start pointer up if its below. If its the same, continue to move the start pointer up
                    start += 1
                else:
                    end -= 1
        finalresult = []
        for sums in result: 
            finalresult.append(list(sums))
        return finalresult


        