class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = {}
        for index in range(len(nums)):
            # loop through the list

            # if current indexed number is in dictionary
            # identified a sum pair that sum to target value
            if nums[index] in summ: 
                return [summ[nums[index]], index]
            
            # if current index value is not in dictionary
            # calculate value needed to sum up to target and use that as key.
            # store current index as value
            summ[target - nums[index]] = index
        return None

        