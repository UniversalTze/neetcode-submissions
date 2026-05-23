class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # do from left to rigth first. 
        result = []
        prev = 0
        for i in range(len(nums)): # 1 [1, 2, 3, 4]
            if i == 0: # envision a product of 1 on the outside of the array 
                # as first element does not have left neigbour so we can just place a 1 in the first index
                result.append(1)
                prev = nums[i]
            else: 
                # store operation of current prev (previous value in the list) * current index - 1 in left list
                # this would result in this list: 
                # first index is arbitrary one so value is not altered at start of list
                # [1 , 1 * 1 (prev), 1 * 2 (prev), 2 * 3 (prev)] = [1, 1, 2, 6]
                # this means we current have one direction where products of array except self has occured. 
                result.append(prev * result[i - 1])
                prev = nums[i] # change prev to current index for next iteration
        
        # used result instead of left and right
        prev = 0
        for i in range(len(nums) - 1, -1, -1):  # 3,2,1,0
            if i == len(nums) - 1: # at the end, need to multiply it by 1 as last element has no element to the right
                prev = nums[i] # get last element before continuing
                continue # last index does not need to change as products except self has already occured
            result[i] = result[i] * prev
            prev = prev * nums[i] # accumulate previous product with current index
        return result

        